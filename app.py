import math
import time
import sqlite3
import secrets
import markupsafe
from flask import Flask
from flask import g, abort, flash, make_response, redirect, render_template, request, session
import config
import reviews
import users


app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    print("elapsed time:", elapsed_time, "s")
    return response

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    page_size = 10
    review_count = reviews.review_count()
    page_count = math.ceil(review_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    all_reviews = reviews.get_reviews(page, page_size)
    return render_template("index.html", page=page, page_count=page_count, items=all_reviews)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    all_reviews = users.get_reviews(user_id)
    return render_template("show_user.html", user=user, reviews=all_reviews)

@app.route("/search_item")
def search_item():
    query = request.args.get("query")
    page = int(request.args.get("page", 1))
    page_size = 10
    result_count = reviews.search_count(query) if query else 0
    page_count = math.ceil(result_count / page_size)
    page_count = max(page_count, 1)

    results = reviews.search_reviews(query, page, page_size) if query else []
    return render_template("search_item.html", page=page,
                           page_count=page_count, query=query, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    classes = reviews.get_classes(item_id)
    messages = reviews.get_messages(item_id)
    images = reviews.get_images(item_id)
    return render_template("show_item.html", item=item,
                           classes=classes, messages=messages, images=images)

@app.route("/image/<int:image_id>")
def show_image(image_id):
    image = reviews.get_image(image_id)
    if not image:
        abort(404)

    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/jpeg")
    return response

@app.route("/images/<int:item_id>")
def edit_images(item_id):
    require_login()
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    images = reviews.get_images(item_id)

    return render_template("images.html", item=item, images=images)

@app.route("/add_image", methods=["POST"])
def add_image():
    require_login()
    check_csrf()

    item_id = request.form["item_id"]
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    file = request.files["image"]
    if not file.filename.endswith(".jpg"):
        flash("VIRHE: Väärä tiedostomuoto")
        return redirect("/images/" + str(item_id))

    image = file.read()
    if len(image) > 100 * 1024:
        flash("VIRHE: Liian suuri kuva")
        return redirect("/images/" + str(item_id))

    reviews.add_image(item_id, image)
    return redirect("/images/" + str(item_id))

@app.route("/remove_images", methods=["POST"])
def remove_images():
    require_login()
    check_csrf()

    item_id = request.form["item_id"]
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    for image_id in request.form.getlist("image_id"):
        reviews.remove_image(item_id, image_id)

    return redirect("/images/" + str(item_id))

@app.route("/create_message", methods=["POST"])
def create_message():
    require_login()
    check_csrf()

    content = request.form["content"]
    if not content or len(content) > 5000:
        abort(403)
    item_id = request.form["item_id"]
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    user_id = session["user_id"]

    reviews.add_message(item_id, user_id, content)

    return redirect("/item/" + str(item_id))

@app.route("/edit_message/<int:message_id>", methods=["GET", "POST"])
def edit_message(message_id):
    require_login()

    message = reviews.get_message(message_id)
    if not message or message["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_message.html", message=message)

    if request.method == "POST":
        check_csrf()
        content = request.form["content"]
        if not content or  len(content) > 5000:
            abort(403)
        reviews.update_message(message["id"], content)
        return redirect("/item/" + str(message["item_id"]))

@app.route("/remove_message/<int:message_id>", methods=["GET", "POST"])
def remove_message(message_id):
    require_login()

    message = reviews.get_message(message_id)
    if not message or message["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_message.html", message=message)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            reviews.remove_message(message["id"])
        return redirect("/item/" + str(message["item_id"]))

@app.route("/new_item")
def new_item():
    require_login()
    classes = reviews.get_all_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    check_csrf()
    title = request.form["title"]
    if not title or  len(title) > 150:
        abort(403)
    review_text = request.form["review_text"]
    if not review_text or len(review_text) > 5000:
        abort(403)
    user_id = session["user_id"]

    all_classes = reviews.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    item_id = reviews.add_review(title, review_text, user_id, classes)

    return redirect("/item/" + str(item_id))

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    classes = reviews.get_all_classes()
    selected_classes = {}
    for my_class in classes:
        selected_classes[my_class] = ""
    for entry in reviews.get_classes(item_id):
        selected_classes[entry["title"]] = entry["value"]
    return render_template("edit_item.html", item=item,
                           selected_classes=selected_classes, classes=classes)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
    check_csrf()
    item_id = request.form["item_id"]
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    if not title or  len(title) > 150:
        abort(403)
    review_text = request.form["review_text"]
    if not review_text or  len(review_text) > 5000:
        abort(403)

    all_classes = reviews.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    reviews.update_review(item_id, title, review_text, classes)

    return redirect("/item/" + str(item_id))

@app.route("/delete_item/<int:item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    require_login()
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("delete_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "delete" in request.form:
            reviews.delete_review(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 3 or len(username) > 20:
        flash("VIRHE: Käyttäjänimen pituus tulee olla 3-20  merkkiä")
        return redirect("/register")
    if len(password1) < 5:
        flash("VIRHE: Salasanan tulee olla vähintään 5 merkkiä")
        return redirect("/register")
    if password1 != password2:
        flash("VIRHE: Salasanat eivät ole samat")
        return redirect("/register")
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: Tunnus on jo varattu")
        return redirect("/register")

    flash("Rekisteröityminen onnistui!")
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            flash("Kirjautuminen onnistui!")
            return redirect("/")
        else:
            flash("VIRHE: Väärä tunnus tai salasana")
            return redirect("/login")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    flash("Olet nyt kirjautunut ulos")
    return redirect("/")

import secrets
import sqlite3
from flask import Flask
from flask import abort, flash, make_response, redirect, render_template, request, session
import config
import db
import reviews
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def index():
    all_reviews = reviews.get_reviews()
    return render_template("index.html", items=all_reviews)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    reviews = users.get_reviews(user_id)
    return render_template("show_user.html", user=user, reviews=reviews)

@app.route("/search_item")
def search_item():
    query = request.args.get("query")
    results = reviews.search_reviews(query) if query else []
    return render_template("search_item.html", query=query, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    genres = reviews.get_genres(item_id)
    messages = reviews.get_messages(item_id)
    images = reviews.get_images(item_id)
    return render_template("show_item.html", item=item, genres=genres, messages=messages, images=images)

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

@app.route("/new_item")
def new_item():
    require_login()
    classes = reviews.get_classes()
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

    all_classes = reviews.get_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            if parts[0] not in all_classes:
                abort(403)
            if parts[1] not in all_classes[parts[0]]:
                abort(403)
            classes.append((parts[0], parts[1]))

    reviews.add_review(title, review_text, user_id, classes)

    item_id = db.last_insert_id()
    return redirect("/item/" + str(item_id))

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    
    classes = reviews.get_classes()
    selected_classes = {}
    for my_class in classes:
        selected_classes[my_class] = ""
    for entry in reviews.get_genres(item_id):
        selected_classes[entry["title"]] = entry["value"]
    return render_template("edit_item.html", item=item, selected_classes=selected_classes, classes=classes)

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

    all_classes = reviews.get_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            if parts[0] not in all_classes:
                abort(403)
            if parts[1] not in all_classes[parts[0]]:
                abort(403)
            classes.append((parts[0], parts[1]))

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
    if password1 != password2:
        flash("VIRHE: Salasanat eivät ole samat")
        return redirect("/register")
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: Tunnus on jo varattu")
        return redirect("/register")

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
            return redirect("/")
        else:
            flash("VIRHE: Väärä tunnus tai salasana")
            return redirect("/login")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")

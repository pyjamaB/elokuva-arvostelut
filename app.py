import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
import config
import db
import reviews
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
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
    return render_template("show_item.html", item=item, genres=genres)

@app.route("/new_item")
def new_item():
    require_login()
    classes = reviews.get_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    title = request.form["title"]
    if not title or  len(title) > 150:
        abort(403)
    review_text = request.form["review_text"]
    if not review_text or len(review_text) > 5000:
        abort(403)
    user_id = session["user_id"]

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            classes.append((parts[0], parts[1]))

    reviews.add_review(title, review_text, user_id, classes)

    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = reviews.get_review(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_item.html", item=item)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
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

    reviews.update_review(item_id, title, review_text)

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
        return "VIRHE: salasanat eivät ole samat"
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"
    return "Tunnus luotu"

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
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")

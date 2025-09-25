import db

def get_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_review(title, review_text, user_id, classes):
    sql = """INSERT INTO items (title, review_text, user_id) VALUES (?, ?, ?)"""
    db.execute(sql, [title, review_text, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO genre_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def get_genres(item_id):
    sql = "SELECT title, value FROM genre_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_reviews():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return  db.query(sql)

def get_review(item_id):
    sql = """SELECT items.id, items.title, items.review_text, users.id user_id, users.username FROM items, users WHERE items.user_id = users.id AND items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_review(item_id, title, review_text, classes):
    sql= """UPDATE items SET title = ?, review_text = ? WHERE id = ?"""
    db.execute(sql, [title, review_text, item_id])

    sql = "DELETE FROM genre_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO genre_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def delete_review(item_id):
    sql = "DELETE FROM genre_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql= "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def search_reviews(query):
    sql = """SELECT id, title FROM items WHERE review_text LIKE ? OR title LIKE ? ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

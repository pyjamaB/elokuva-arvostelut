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

def add_message(item_id, user_id, content):
    sql = """INSERT INTO messages (item_id, user_id, content) VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, content])

def get_messages(item_id):
    sql = """SELECT messages.content, users.id user_id, users.username
             FROM messages, users
             WHERE messages.item_id = ? AND messages.user_id = users.id
             ORDER BY messages.id DESC"""
    return db.query(sql, [item_id])

def get_genres(item_id):
    sql = "SELECT title, value FROM genre_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_reviews():
    sql = """SELECT items.id, items.title, users.id user_id, users.username
             FROM items, users WHERE items.user_id = users.id ORDER BY items.id DESC"""
    return  db.query(sql)

def get_review(item_id):
    sql = """SELECT items.id, items.title, items.review_text, users.id user_id, users.username
             FROM items, users WHERE items.user_id = users.id AND items.id = ?"""
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
    sql= "DELETE FROM messages WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql= "DELETE FROM images WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM genre_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql= "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def search_reviews(query):
    sql = """SELECT id, title FROM items WHERE review_text LIKE ? OR title LIKE ? ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def get_images(item_id):
    sql = "SELECT id FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND  item_id = ?"
    db.execute(sql, [image_id, item_id])

import db

def add_review(title, review_text, user_id):
    sql = """INSERT INTO items (title, review_text, user_id) VALUES (?, ?, ?)"""
    db.execute(sql, [title, review_text, user_id])

def get_reviews():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return  db.query(sql)

def get_review(item_id):
    sql = """SELECT items.id, items.title, items.review_text, users.id user_id, users.username FROM items, users WHERE items.user_id = users.id AND items.id = ?"""
    return db.query(sql, [item_id])[0]

def update_review(item_id, title, review_text):
    sql= """UPDATE items SET title = ?, review_text = ? WHERE id = ?"""
    db.execute(sql, [title, review_text, item_id])

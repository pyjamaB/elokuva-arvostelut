import db

def add_review(title, review_text, user_id):
    sql = """INSERT INTO items (title, review_text, user_id) VALUES (?, ?, ?)"""
    db.execute(sql, [title, review_text, user_id])

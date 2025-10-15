import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM messages")

USER_COUNT = 1000
REVIEW_COUNT = 10**5
MESSAGE_COUNT = 10**6

for i in range(1, USER_COUNT + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, REVIEW_COUNT + 1):
    user_id = random.randint(1, USER_COUNT)
    db.execute("INSERT INTO items (title, review_text, user_id) VALUES (?, ?, ?)",
               ["review" + str(i), "review_text" + str(i), user_id])

for i in range(1, MESSAGE_COUNT + 1):
    user_id = random.randint(1, USER_COUNT)
    item_id = random.randint(1, REVIEW_COUNT)
    db.execute("""INSERT INTO messages (item_id, user_id, content)
                  VALUES (?, ?, ?)""",
               [item_id, user_id, "message" + str(i)])

db.commit()
db.close()

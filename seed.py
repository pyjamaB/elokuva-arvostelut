import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM messages")

user_count = 1000
review_count = 10**5
message_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, review_count + 1):
    user_id = random.randint(1, user_count)
    db.execute("INSERT INTO items (title, review_text, user_id) VALUES (?, ?, ?)",
               ["review" + str(i), "review_text" + str(i), user_id])

for i in range(1, message_count + 1):
    user_id = random.randint(1, user_count)
    item_id = random.randint(1, review_count)
    db.execute("""INSERT INTO messages (item_id, user_id, content)
                  VALUES (?, ?, ?)""",
               [item_id, user_id, "message" + str(i)])

db.commit()
db.close()

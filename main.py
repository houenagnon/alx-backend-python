import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER, mail TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'alice', 20, 'alice@a.com')")
cursor.execute("INSERT INTO users VALUES (2,'bob', 30, 'bob@b.com')")
cursor.execute("INSERT INTO users VALUES (3, 'eve', 40, 'eve@e.com')")

connection.commit()

print(connection.total_changes)
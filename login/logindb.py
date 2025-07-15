import sqlite3

# Create a database connection
conn = sqlite3.connect("login.db")
cursor = conn.cursor()

# Create a table for storing user credentials
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

conn.commit()
conn.close()

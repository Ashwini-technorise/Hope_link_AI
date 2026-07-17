import sqlite3

conn = sqlite3.connect("hopelink.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS missing_persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    location TEXT,
    date_missing TEXT,
    description TEXT,
    photo TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
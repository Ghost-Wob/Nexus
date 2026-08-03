from app.database.database import Database

db = Database()

db.execute("""
CREATE TABLE IF NOT EXISTS concepts(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT UNIQUE,

    slug TEXT UNIQUE,

    category TEXT,

    markdown TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

print("Database initialized.")

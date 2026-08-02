import sqlite3

DB_PATH = "database/nexus.db"


def create_database():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS concepts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        language TEXT,
        level INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relations (
        id INTEGER PRIMARY KEY,
        source TEXT,
        relation TEXT,
        target TEXT,
        weight REAL
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()

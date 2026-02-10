import sqlite3

DB_NAME = "chat.db"

def get_connection():
    """
    Create and return a database connection
    """
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def create_table():
    """
    Create chats table if it does not exist
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            message TEXT,
            reply TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_chat(user, message, reply):
    """
    Save a chat message to database
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (user, message, reply) VALUES (?, ?, ?)",
        (user, message, reply)
    )

    conn.commit()
    conn.close()

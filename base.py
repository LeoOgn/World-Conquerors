from sqlite3 import connect


connection = connect("db.db")
create_users = """
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY,
        name VARCHAR(255),
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
create_characters = """
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        streight INTEGER DEFAULT 1,
        agility INTEGER DEFAULT 1,
        physique INTEGER DEFAULT 1,
        level INTEGER DEFAULT 1,
        balance INTEGER DEFAULT 0,
        experience INTEGER DEFAULT 0,
        current_health INTEGER DEFAULT 5,
        user_id INTEGER NOT NULL,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""
cursor = connection.cursor()
cursor.execute(create_users)
cursor.execute(create_characters)
connection.commit()
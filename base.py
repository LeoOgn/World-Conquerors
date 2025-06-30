from sqlite3 import connect


connection = connect("db.db")
sql = """
    CREATE TABLE IF NOTE EXISTS users (
        id BIGINT PRIMARY KEY,
        name VARCHAR(255),
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
cursor = connection.cursor()
cursor.execute(sql)
connection.commit()
from sqlite3 import connect
from seeds.location_seed import seed_locations
from seeds.mob_seed import seed_mobs


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
        streight INTEGER DEFAULT 0,
        agility INTEGER DEFAULT 0,
        physique INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        balance INTEGER DEFAULT 0,
        experience INTEGER DEFAULT 0,
        current_health INTEGER DEFAULT 5,
        user_id INTEGER NOT NULL,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""
create_locations = """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255),
        level_from INTEGER,
        level_to INTEGER,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
create_mobs = """
    CREATE TABLE IF NOT EXISTS mobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        streight INTEGER DEFAULT 0,
        agility INTEGER DEFAULT 0,
        physique INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        location_id INTEGER,
        exp INTEGER DEFAULT 0,
        FOREIGN KEY (location_id) REFERENCES locations (id)
    );
"""
create_equipment = """
    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255),
        bonus_streight INTEGER DEFAULT 0,
        bonus_agility INTEGER DEFAULT 0,
        bonus_physique INTEGER DEFAULT 0,
        must_level INTEGER DEFAULT 1,
        must_physique INTEGER DEFAULT 0,
        must_streight INTEGER DEFAULT 0,
        must_agility INTEGER DEFAULT 0,
        attack INTEGER DEFAULT 0,
        defend INTEGER DEFAULT 0,
        price INTEGER DEFAULT 0,
        rare VARCHAR(255),
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
cursor = connection.cursor()
cursor.execute(create_users)
cursor.execute(create_characters)
cursor.execute(create_locations)
cursor.execute(create_mobs)
cursor.execute(create_equipment)
connection.commit()

seed_locations()
seed_mobs()
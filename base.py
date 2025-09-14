# from sqlite3 import connect
from repositories import connection
from seeds.location_seed import seed_locations
from seeds.mob_seed import seed_mobs
from seeds.equipment_seed import seed_equipment_sets, seed_equipment_types, seed_equipments
from seeds.item_seed import seed_items


# connection = connect("db.db")
create_users = """
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
create_characters = """
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        streight INTEGER DEFAULT 0,
        agility INTEGER DEFAULT 0,
        physique INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        balance INTEGER DEFAULT 0,
        experience INTEGER DEFAULT 0,
        current_health INTEGER DEFAULT 5,
        available_scores INTEGER DEFAULT 5,
        user_id BIGINT NOT NULL,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
"""
create_locations = """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        level_from INTEGER,
        level_to INTEGER,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
create_mobs = """
    CREATE TABLE IF NOT EXISTS mobs (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
create_equipment_types = """
    CREATE TABLE IF NOT EXISTS equipment_types (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255)
    );
"""
create_equipment_sets = """
    CREATE TABLE IF NOT EXISTS equipment_sets (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        bonus_streight INTEGER DEFAULT 0,
        bonus_agility INTEGER DEFAULT 0,
        bonus_physique INTEGER DEFAULT 0
    );
"""
create_equipment = """
    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
        equipment_type_id INTEGER NOT NULL,
        equipment_set_id INTEGER DEFAULT NULL,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (equipment_type_id) REFERENCES equipment_types (id),
        FOREIGN KEY (equipment_set_id) REFERENCES equipment_sets (id)
    );
"""
create_items = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        rare VARCHAR(255),
        description TEXT,
        price INTEGER DEFAULT 0,
        equipment_id INTEGER,
        image VARCHAR(255),
        FOREIGN KEY (equipment_id) REFERENCES equipment (id)
    );
"""
create_inventory = """
    CREATE TABLE IF NOT EXISTS inventory (
        character_id INTEGER,
        item_id INTEGER,
        count INTEGER DEFAULT 1,
        is_equiped BOOLEAN DEFAULT FALSE,
        PRIMARY KEY (character_id, item_id),
        FOREIGN KEY (character_id) REFERENCES characters (id),
        FOREIGN KEY (item_id) REFERENCES items (id)
    );
"""
create_loot = """
    CREATE TABLE IF NOT EXISTS loot (
        mob_id INTEGER,
        item_id INTEGER,
        chance FLOAT,
        PRIMARY KEY (mob_id, item_id),
        FOREIGN KEY (mob_id) REFERENCES mobs (id),
        FOREIGN KEY (item_id) REFERENCES items (id)
    );
"""

cursor = connection.cursor()
cursor.execute(create_users)
cursor.execute(create_characters)
cursor.execute(create_locations)
cursor.execute(create_mobs)
cursor.execute(create_equipment_types)
cursor.execute(create_equipment_sets)
cursor.execute(create_equipment)
cursor.execute(create_items)
cursor.execute(create_inventory)
cursor.execute(create_loot)
connection.commit()

seed_locations()
seed_mobs()
seed_equipment_types()
seed_equipment_sets()
seed_equipments()
seed_items()
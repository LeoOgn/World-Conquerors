from sqlite3 import connect
from repositories import MobRepository


MOBS = [
    {"name": "Безобидная гусеница", "streight" : 1, "agility" : 0, "physique" : 1, "level" : 1, "location_id" : 1},
    {"name": "Саблезубый заяц", "streight" : 1, "agility" : 1, "physique" : 1, "level" : 2, "location_id" : 1},
    {"name": "Остроклювая курица", "streight" : 2, "agility" : 3, "physique" : 2, "level" : 3, "location_id" : 1},
    {"name": "Свирепый лис", "streight" : 2, "agility" : 5, "physique" : 2, "level" : 4, "location_id" : 1},
    {"name": "Злой волк", "streight" : 3, "agility" : 10, "physique" : 3, "level" : 5, "location_id" : 1},
]

def seed_mobs(mobs=MOBS):
    connection = connect("db.db")
    repo = MobRepository(connection)

    for mob in mobs:
        repo.create(**mob)
        print(f"Моб {mob["name"]} создан")
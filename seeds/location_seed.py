from sqlite3 import connect
from repositories import LocationRepository


LOCATIONS = [
    {"title": "Луг перед город", "level_from" : 1, "level_to" : 5},
    {"title": "Поляна перед лесом", "level_from" : 6, "level_to" : 10},
    {"title": "Светлая часть леса", "level_from" : 11, "level_to" : 20},
]

def seed_locations(locations=LOCATIONS):
    connection = connect("db.db")
    repo = LocationRepository(connection)

    for location in locations:
        repo.create(**location)
        print(f"Локация {location["title"]} создана")

from sqlite3 import connect
from repositories import LocationRepository


LOCATIONS = [
    {"title": "Луг за городом", "level_from" : 1, "level_to" : 5},
    {"title": "Темный лес", "level_from" : 6, "level_to" : 10},
    {"title": "Ущелье Краула", "level_from" : 11, "level_to" : 15},
]

def seed_locations(locations=LOCATIONS):
    connection = connect("db.db")
    repo = LocationRepository(connection)
    repo.clear()
    for location in locations:
        repo.create(**location)
        print(f"Локация {location["title"]} создана")

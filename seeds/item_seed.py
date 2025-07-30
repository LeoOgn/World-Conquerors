from sqlite3 import connect
from repositories import ItemRepository


ITEMS = [
    {"title": "Ключ от обычного сундука"},
    {"title": "Ключ от необычного сундука"},
    {"title": "Ключ от редкого сундука"},
    {"title": "Ключ от эпического сундука"},
    {"title": "Ключ от легендарного сундука"},
    {"title": "Ключ от реликтового сундука"}

]

def seed_items(items=ITEMS, start=0, end=len(ITEMS)):
    connection = connect("db.db")
    repo = ItemRepository(connection)
    
    for item in items[start:end]:
        repo.create(**item)
        print(f"Предмет {item["title"]} создан")
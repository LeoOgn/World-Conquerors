from sqlite3 import connect
from repositories import ItemRepository


ITEMS = [
    {"title": "Ключ от обычного сундука", "rare" : "Обычное"},
    {"title": "Ключ от необычного сундука", "rare" : "Необычное"},
    {"title": "Ключ от редкого сундука", "rare" : "Редкое"},
    {"title": "Ключ от эпического сундука", "rare" : "Эпическое"},
    {"title": "Ключ от легендарного сундука", "rare" : "Легендарное"},
    {"title": "Ключ от реликтового сундука", "rare" : "Реликтовое"}

]

def seed_items(items=ITEMS, start=0, end=len(ITEMS)):
    connection = connect("db.db")
    repo = ItemRepository(connection)
    
    for item in items[start:end]:
        repo.create(**item)
        print(f"Предмет {item["title"]} создан")
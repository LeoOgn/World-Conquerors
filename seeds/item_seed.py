from sqlite3 import connect
from repositories import ItemRepository


ITEMS = [
    {"title": "Ключ от обычного сундука", "rare" : "Обычное", "price": 1, "description" : "", "image" : "images/Ключ от необычного сундука.png"},
    {"title": "Ключ от необычного сундука", "rare" : "Необычное", "price": 10, "description" : "", "image" : "images/Ключ от обычного сундука.png"},
    {"title": "Ключ от редкого сундука", "rare" : "Редкое", "price": 100, "description" : "", "image" : "images/Ключ от редкого сундука.png"},
    {"title": "Ключ от эпического сундука", "rare" : "Эпическое", "price": 1000, "description" : "", "image" : ""},
    {"title": "Ключ от легендарного сундука", "rare" : "Легендарное", "price": 10000, "description" : "", "image" : ""},
    {"title": "Ключ от реликтового сундука", "rare" : "Реликтовое", "price": 100000, "description" : "", "image" : ""}

]

def seed_items(items=ITEMS, start=0, end=len(ITEMS)):
    connection = connect("db.db")
    repo = ItemRepository(connection)
    
    for item in items[start:end]:
        repo.create(**item)
        print(f"Предмет {item["title"]} создан")
from sqlite3 import connect
from repositories import MobRepository


MOBS = [
    {"name": "Гусеница", "streight" : 3, "agility" : 0, "physique" : 2, "level" : 1, "location_id" : 1, "exp" : 0},
    {"name": "Мышь", "streight" : 1, "agility" : 3, "physique" : 1, "level" : 1, "location_id" : 1, "exp" : 0},
    {"name": "Заяц", "streight" : 3, "agility" : 5, "physique" : 2, "level" : 2, "location_id" : 1, "exp" : 0},
    {"name": "Гусь", "streight" : 4, "agility" : 3, "physique" : 3, "level" : 2, "location_id" : 1, "exp" : 0},
    {"name": "Курица", "streight" : 3, "agility" : 10, "physique" : 2, "level" : 3, "location_id" : 1, "exp" : 0},
    {"name": "Бурундук", "streight" : 5, "agility" : 9, "physique" : 1, "level" : 3, "location_id" : 1, "exp" : 0},
    {"name": "Лис", "streight" : 11, "agility" : 0, "physique" : 9, "level" : 4, "location_id" : 1, "exp" : 0},
    {"name": "Скунс", "streight" : 15, "agility" : 0, "physique" : 5, "level" : 4, "location_id" : 1, "exp" : 0},
    {"name": "Волк", "streight" : 10, "agility" : 10, "physique" : 5, "level" : 5, "location_id" : 1, "exp" : 0},
    {"name": "Мишка", "streight" : 15, "agility" : 0, "physique" : 10, "level" : 5, "location_id" : 1, "exp" : 0},
    {"name": "Гигантский крыс", "streight" : 5, "agility" : 20, "physique" : 5, "level" : 6, "location_id" : 2, "exp" : 0},
    {"name": "Стервятник", "streight" : 10, "agility" : 10, "physique" : 10, "level" : 6, "location_id" : 2, "exp" : 0},
    {"name": "Лисолюд", "streight" : 10, "agility" : 20, "physique" : 5, "level" : 7, "location_id" : 2, "exp" : 0},
    {"name": "Акулон", "streight" : 20, "agility" : 0, "physique" : 15, "level" : 7, "location_id" : 2, "exp" : 0},
    {"name": "Гигантский паук", "streight" : 10, "agility" : 20, "physique" : 10, "level" : 8, "location_id" : 2, "exp" : 0},
    {"name": "Минотавр", "streight" : 20, "agility" : 0, "physique" : 20, "level" : 8, "location_id" : 2, "exp" : 0},
    {"name": "Циклоп", "streight" : 5, "agility" : 0, "physique" : 40, "level" : 9, "location_id" : 2, "exp" : 0},
    {"name": "Оборотень", "streight" : 15, "agility" : 10, "physique" : 20, "level" : 9, "location_id" : 2, "exp" : 0},
    {"name": "Разоритель", "streight" : 49, "agility" : 0, "physique" : 1, "level" : 10, "location_id" : 2, "exp" : 0},
    {"name": "Младший демон", "streight" : 7, "agility" : 40, "physique" : 3, "level" : 10, "location_id" : 2, "exp" : 0},
    {"name": "Зомби", "streight" : 30, "agility" : 5, "physique" : 20, "level" : 11, "location_id" : 3, "exp" : 0},
    {"name": "Пещерный червь", "streight" : 20, "agility" : 30, "physique" : 5, "level" : 11, "location_id" : 3, "exp" : 0},
    {"name": "Каменный голем", "streight" : 10, "agility" : 0, "physique" : 50, "level" : 12, "location_id" : 3, "exp" : 0},
    {"name": "Ящер", "streight" : 5, "agility" : 50, "physique" : 5, "level" : 12, "location_id" : 3, "exp" : 0},
    {"name": "Матерый ящер", "streight" : 10, "agility" : 45, "physique" : 10, "level" : 13, "location_id" : 3, "exp" : 0},
    {"name": "Огр", "streight" : 50, "agility" : 0, "physique" : 15, "level" : 13, "location_id" : 3, "exp" : 0},
    {"name": "Великан", "streight" : 5, "agility" : 50, "physique" : 5, "level" : 14, "location_id" : 3, "exp" : 0},
    {"name": "Бешеный гном Федя", "streight" : 15, "agility" : 50, "physique" : 10, "level" : 15, "location_id" : 3, "exp" : 0},
]

def seed_mobs(mobs=MOBS, start=0, end=len(MOBS)):
    connection = connect("db.db")
    repo = MobRepository(connection)

    for mob in mobs[start:end]:
        repo.create(**mob)
        print(f"Моб {mob["name"]} создан")
from sqlite3 import connect
from repositories import MobRepository


MOBS = [
    {"name": "Гусеница", "streight" : 3, "agility" : 0, "physique" : 2, "level" : 1, "location_id" : 1, "exp" : 1},
    {"name": "Мышь", "streight" : 1, "agility" : 3, "physique" : 1, "level" : 1, "location_id" : 1, "exp" : 1},
    {"name": "Заяц", "streight" : 3, "agility" : 5, "physique" : 2, "level" : 2, "location_id" : 1, "exp" : 2},
    {"name": "Гусь", "streight" : 4, "agility" : 3, "physique" : 3, "level" : 2, "location_id" : 1, "exp" : 2},
    {"name": "Курица", "streight" : 3, "agility" : 10, "physique" : 2, "level" : 3, "location_id" : 1, "exp" : 3},
    {"name": "Бурундук", "streight" : 5, "agility" : 9, "physique" : 1, "level" : 3, "location_id" : 1, "exp" : 3},
    {"name": "Лис", "streight" : 11, "agility" : 0, "physique" : 9, "level" : 4, "location_id" : 1, "exp" : 5},
    {"name": "Скунс", "streight" : 15, "agility" : 0, "physique" : 5, "level" : 4, "location_id" : 1, "exp" : 5},
    {"name": "Волк", "streight" : 10, "agility" : 10, "physique" : 5, "level" : 5, "location_id" : 1, "exp" : 8},
    {"name": "Мишка", "streight" : 15, "agility" : 0, "physique" : 10, "level" : 5, "location_id" : 1, "exp" : 8},
    {"name": "Гигантский крыс", "streight" : 5, "agility" : 20, "physique" : 5, "level" : 6, "location_id" : 2, "exp" : 12},
    {"name": "Стервятник", "streight" : 10, "agility" : 10, "physique" : 10, "level" : 6, "location_id" : 2, "exp" : 12},
    {"name": "Лисолюд", "streight" : 10, "agility" : 20, "physique" : 5, "level" : 7, "location_id" : 2, "exp" : 20},
    {"name": "Акулон", "streight" : 20, "agility" : 0, "physique" : 15, "level" : 7, "location_id" : 2, "exp" : 20},
    {"name": "Гигантский паук", "streight" : 10, "agility" : 20, "physique" : 10, "level" : 8, "location_id" : 2, "exp" : 30},
    {"name": "Минотавр", "streight" : 20, "agility" : 0, "physique" : 20, "level" : 8, "location_id" : 2, "exp" : 30},
    {"name": "Циклоп", "streight" : 5, "agility" : 0, "physique" : 40, "level" : 9, "location_id" : 2, "exp" : 50},
    {"name": "Оборотень", "streight" : 15, "agility" : 10, "physique" : 20, "level" : 9, "location_id" : 2, "exp" : 50},
    {"name": "Разоритель", "streight" : 49, "agility" : 0, "physique" : 1, "level" : 10, "location_id" : 2, "exp" : 75},
    {"name": "Младший демон", "streight" : 7, "agility" : 40, "physique" : 3, "level" : 10, "location_id" : 2, "exp" : 75},
    {"name": "Зомби", "streight" : 30, "agility" : 5, "physique" : 20, "level" : 11, "location_id" : 3, "exp" : 125},
    {"name": "Пещерный червь", "streight" : 20, "agility" : 30, "physique" : 5, "level" : 11, "location_id" : 3, "exp" : 125},
    {"name": "Каменный голем", "streight" : 10, "agility" : 0, "physique" : 50, "level" : 12, "location_id" : 3, "exp" : 225},
    {"name": "Ящер", "streight" : 5, "agility" : 50, "physique" : 5, "level" : 12, "location_id" : 3, "exp" : 225},
    {"name": "Матерый ящер", "streight" : 10, "agility" : 45, "physique" : 10, "level" : 13, "location_id" : 3, "exp" : 450},
    {"name": "Огр", "streight" : 50, "agility" : 0, "physique" : 15, "level" : 13, "location_id" : 3, "exp" : 450},
    {"name": "Великан", "streight" : 5, "agility" : 50, "physique" : 5, "level" : 14, "location_id" : 3, "exp" : 750},
    {"name": "Камнелюд", "streight" : 10, "agility" : 0, "physique" : 60, "level" : 14, "location_id" : 3, "exp" : 750},
    {"name": "Пещерный паук", "streight" : 10, "agility" : 0, "physique" : 60, "level" : 15, "location_id" : 3, "exp" : 1250},
    {"name": "Веселый Краул", "streight" : 40, "agility" : 20, "physique" : 40, "level" : 20, "location_id" : 3, "exp" : 10000},
    {"name": "Бешеный гном Федя", "streight" : 25, "agility" : 50, "physique" : 25, "level" : 20, "location_id" : 3, "exp" : 0},
    {"name": "Каменюка", "streight" : 20, "agility" : 0, "physique" : 60, "level" : 16, "location_id" : 4, "exp" : 2000},
    {"name": "Летучий кровосос", "streight" : 10, "agility" : 60, "physique" : 10, "level" : 16, "location_id" : 4, "exp" : 2000},
    {"name": "Свирепый крот", "streight" : 50, "agility" : 0, "physique" : 35, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Водный кусач", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Пещерный сыч", "streight" : 60, "agility" : 0, "physique" : 30, "level" : 18, "location_id" : 4, "exp" : 4500},
    {"name": "Каменный оцелот", "streight" : 40, "agility" : 0, "physique" : 50, "level" : 18, "location_id" : 4, "exp" : 4500},
    {"name": "Алмазный жук", "streight" : 5, "agility" : 0, "physique" : 90, "level" : 19, "location_id" : 4, "exp" : 7000},
    {"name": "Бриллиантовый жук", "streight" : 10, "agility" : 0, "physique" : 85, "level" : 19, "location_id" : 4, "exp" : 7000},
    {"name": "Королева жуков", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 20, "location_id" : 4, "exp" : 10000},
    {"name": "Рогдар", "streight" : 4, "agility" : 120, "physique" : 1, "level" : 25, "location_id" : 4, "exp" : 180000},
    {"name": "Кривозуб", "streight" : 5, "agility" : 50, "physique" : 50, "level" : 21, "location_id" : 5, "exp" : 15000},
    {"name": "Адамантитовый аист", "streight" : 70, "agility" : 0, "physique" : 35, "level" : 21, "location_id" : 5, "exp" : 15000},
    {"name": "Жаба", "streight" : 30, "agility" : 0, "physique" : 80, "level" : 22, "location_id" : 5, "exp" : 20000},
    {"name": "Комар", "streight" : 1, "agility" : 108, "physique" : 1, "level" : 22, "location_id" : 5, "exp" : 20000},
    {"name": "Летун", "streight" : 20, "agility" : 80, "physique" : 5, "level" : 23, "location_id" : 5, "exp" : 30000},
    {"name": "Пиявка", "streight" : 4, "agility" : 120, "physique" : 1, "level" : 23, "location_id" : 5, "exp" : 30000},
    {"name": "Русалка", "streight" : 4, "agility" : 120, "physique" : 1, "level" : 24, "location_id" : 5, "exp" : 45000},
    {"name": "Болотник", "streight" : 4, "agility" : 120, "physique" : 1, "level" : 24, "location_id" : 5, "exp" : 45000},
    {"name": "Кикимора", "streight" : 4, "agility" : 120, "physique" : 1, "level" : 25, "location_id" : 5, "exp" : 70000},
    {"name": "Торфу - болотный бог", "streight" : 1, "agility" : 498, "physique" : 1, "level" : 100, "location_id" : 5, "exp" : 2000000},

    # Мобы для подземелья "Адское пекло" - 50 уровень
    {"name": "Сатир", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 50, "location_id" : 4, "exp" : 3000},
    {"name": "Инкуб", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 50, "location_id" : 4, "exp" : 3000},
    {"name": "Сукуба", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 50, "location_id" : 4, "exp" : 3000},
    {"name": "Бес", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 50, "location_id" : 4, "exp" : 3000},
    {"name": "Черт", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 50, "location_id" : 4, "exp" : 3000},
    {"name": "Асмодон - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Люцифер - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Сатана - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Вельзевул - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Левиафан - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Маммон - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000},
    {"name": "Бельфегор - босс подземелья", "streight" : 15, "agility" : 60, "physique" : 10, "level" : 17, "location_id" : 4, "exp" : 3000}
]

def seed_mobs(mobs=MOBS, start=0, end=len(MOBS)):
    connection = connect("db.db")
    repo = MobRepository(connection)

    for mob in mobs[start:end]:
        repo.create(**mob)
        print(f"Моб {mob["name"]} создан")
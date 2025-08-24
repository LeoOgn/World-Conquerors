from sqlite3 import connect
from repositories import EquipmentRepository, ItemRepository


EQUIPMENT_TYPES = [
    "Головной убор",
    "Рубашка",
    "Штаны",
    "Ботинки",
    "Кольцо",
    "Меч"
]

EQUIPMENT_SETS = [
    {"title" : "Доспех Теодора", "bonus_streight" : 50, "bonus_agility" : 100, "bonus_physique" : 0},
    {"title" : "Сокровище Святогора", "bonus_streight" : 400, "bonus_agility" : 200, "bonus_physique" : 400},
    {"title" : "Воровской костюм Арно", "bonus_streight" : 0, "bonus_agility" : 100, "bonus_physique" : 0}
]


EQUIPMENTS = [
    {"title" : "Медное кольцо силы", "bonus_streight" : 1, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Медное кольцо ловкости", "bonus_streight" : 0, "bonus_agility" : 1, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Медное кольцо телосложения", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 1, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Серебряное кольцо силы + ловкости", "bonus_streight" : 1, "bonus_agility" : 1, "bonus_physique" : 0, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Серебряное кольцо силы + телосложения", "bonus_streight" : 1, "bonus_agility" : 0, "bonus_physique" : 1, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Серебряное кольцо телосложения + ловкости", "bonus_streight" : 0, "bonus_agility" : 1, "bonus_physique" : 1, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Золотое кольцо всесилия", "bonus_streight" : 2, "bonus_agility" : 2, "bonus_physique" : 2, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 120, "rare" : "Редкое", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Перстень отрицания", "bonus_streight" : 5, "bonus_agility" : 10, "bonus_physique" : 3, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Фейский браслет", "bonus_streight" : 0, "bonus_agility" : 30, "bonus_physique" : 0, "must_level" : 15, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Кольцо ненависти", "bonus_streight" : 15, "bonus_agility" : 0, "bonus_physique" : 10, "must_level" : 7, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Пинг-понг колечко", "bonus_streight" : 1, "bonus_agility" : 25, "bonus_physique" : 2, "must_level" : 7, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Колечко с джином", "bonus_streight" : 30, "bonus_agility" : 10, "bonus_physique" : 20, "must_level" : 10, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Кольцо клоуна", "bonus_streight" : 0, "bonus_agility" : 75, "bonus_physique" : 0, "must_level" : 7, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Кольцо вора", "bonus_streight" : 5, "bonus_agility" : 65, "bonus_physique" : 5, "must_level" : 7, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Кольцо смерти", "bonus_streight" : 50, "bonus_agility" : 15, "bonus_physique" : 20, "must_level" : 15, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : None, "description" : ""},
    {"title" : "Клановая печать Теодора", "bonus_streight" : 50, "bonus_agility" : 80, "bonus_physique" : 20, "must_level" : 30, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 10000, "rare" : "Реликтовое", "equipment_type_id" : 5, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Личная печать Теодора", "bonus_streight" : 70, "bonus_agility" : 50, "bonus_physique" : 30, "must_level" : 30, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 10000, "rare" : "Реликтовое", "equipment_type_id" : 5, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Крокодильи сапоги Теодора", "bonus_streight" : 5, "bonus_agility" : 20, "bonus_physique" : 0, "must_level" : 30, "must_streight" : 40, "must_agility" : 10, "must_physique" : 40, "attack" : 0, "defend" : 30, "price" : 10000, "rare" : "Реликтовое", "equipment_type_id" : 4, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Хитиновые штаны Теодора", "bonus_streight" : 10, "bonus_agility" : 5, "bonus_physique" : 0, "must_level" : 30, "must_streight" : 40, "must_agility" : 0, "must_physique" : 40, "attack" : 0, "defend" : 100, "price" : 10000, "rare" : "Реликтовое", "equipment_type_id" : 3, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Мифриловая куртка Теодора", "bonus_streight" : 5, "bonus_agility" : 25, "bonus_physique" : 30, "must_level" : 30, "must_streight" : 40, "must_agility" : 0, "must_physique" : 40, "attack" : 0, "defend" : 100, "price" : 10000, "rare" : "Реликтовое", "equipment_type_id" : 2, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Адамантитовый шлем Теодора", "bonus_streight" : 0, "bonus_agility" : 40, "bonus_physique" : 0, "must_level" : 35, "must_streight" : 70, "must_agility" : 0, "must_physique" : 60, "attack" : 0, "defend" : 200, "price" : 12000, "rare" : "Реликтовое", "equipment_type_id" : 1, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Лавовые кинжалы Теодора", "bonus_streight" : 0, "bonus_agility" : 50, "bonus_physique" : 0, "must_level" : 40, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 500, "defend" : 0, "price" : 15000, "rare" : "Реликтовое", "equipment_type_id" : 7, "equipment_set_id" : 1, "description" : ""},
    {"title" : "Корыто Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 1, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Покоцаная рубаха Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 2, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Неотесаные штаны Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 3, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Дырявые лапти Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 4, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Окислевшееся кольцо Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Оплавившееся кольцо Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 5, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Сломаные кинжалы Святогора", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 100, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 15000, "rare" : "Легендарное", "equipment_type_id" : 6, "equipment_set_id" : 2, "description" : ""},
    {"title" : "Маска Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 30, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Элегантная рубашка Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 55, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Ченые штаны Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 40, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Бесшумные сапожки Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 30, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Бесшумные сапожки Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 30, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Кольцо для взлома сейфов Арно", "bonus_streight" : 0, "bonus_agility" : 50, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Кольцо для взлома дверей Арно", "bonus_streight" : 0, "bonus_agility" : 50, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 0, "defend" : 0, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""},
    {"title" : "Стелет Арно", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_physique" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_physique" : 0, "attack" : 200, "defend" : 0, "price" : 1000, "rare" : "Эпическое", "equipment_type_id" : 1, "equipment_set_id" : 3, "description" : ""}
]

def seed_equipment_types(equipment_types=EQUIPMENT_TYPES, start=0, end=len(EQUIPMENT_TYPES)):
    connection = connect("db.db")
    repo = EquipmentRepository(connection)

    for equipment_type in equipment_types[start:end]:
        repo.create_type(equipment_type)
        print(f"Тип {equipment_type} создан")

def seed_equipment_sets(equipment_sets=EQUIPMENT_SETS, start=0, end=len(EQUIPMENT_SETS)):
    connection = connect("db.db")
    repo = EquipmentRepository(connection)

    for equipment_set in equipment_sets[start:end]:
        repo.create_set(**equipment_set)
        print(f"Сет {equipment_set["title"]} создан")

def seed_equipments(equipments=EQUIPMENTS, start=0, end=len(EQUIPMENTS)):
    connection = connect("db.db")
    repo = EquipmentRepository(connection)
    item_repo = ItemRepository(connection)

    for i in range(len(equipments[start:end])):
        equipment: dict = equipments[i]
        equipment_creation_dict = equipment.copy()
        equipment_creation_dict.pop("rare")
        equipment_creation_dict.pop("description")
        equipment_creation_dict.pop("price")
        repo.create(**equipment_creation_dict)
        item_repo.create(
            equipment["title"], 
            equipment["rare"], 
            equipment["description"], 
            equipment["price"], 
            equipment_id=i + 1
        )
        print(f"Часть экипировки {equipment["title"]} создана")
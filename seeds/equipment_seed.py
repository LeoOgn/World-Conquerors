from sqlite3 import connect
from repositories import EquipmentRepository


EQUIPMENTS = [
    {"title" : "Медное кольцо силы", "bonus_streight" : 1, "bonus_agility" : 0, "bonus_phisyque" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное"},
    {"title" : "Медное кольцо ловкости", "bonus_streight" : 0, "bonus_agility" : 1, "bonus_phisyque" : 0, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное"},
    {"title" : "Медное кольцо телосложения", "bonus_streight" : 0, "bonus_agility" : 0, "bonus_phisyque" : 1, "must_level" : 1, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 10, "rare" : "Обыкновенное"},
    {"title" : "Серебряное кольцо силы + ловкости", "bonus_streight" : 1, "bonus_agility" : 1, "bonus_phisyque" : 0, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное"},
    {"title" : "Серебряное кольцо силы + телосложения", "bonus_streight" : 1, "bonus_agility" : 0, "bonus_phisyque" : 1, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное"},
    {"title" : "Серебряное кольцо телосложения + ловкости", "bonus_streight" : 0, "bonus_agility" : 1, "bonus_phisyque" : 1, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 30, "rare" : "Необычное"},
    {"title" : "Золотое кольцо всесилия", "bonus_streight" : 2, "bonus_agility" : 2, "bonus_phisyque" : 2, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 120, "rare" : "Редкое"},
    {"title" : "Перстень отрицания", "bonus_streight" : 5, "bonus_agility" : 10, "bonus_phisyque" : 3, "must_level" : 5, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое"},
    {"title" : "Фейский браслет", "bonus_streight" : 0, "bonus_agility" : 40, "bonus_phisyque" : 0, "must_level" : 15, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое"},
    {"title" : "Кольцо ненависти", "bonus_streight" : 15, "bonus_agility" : 0, "bonus_phisyque" : 10, "must_level" : 7, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Эпическое"},
    {"title" : "Колечко с джином", "bonus_streight" : 30, "bonus_agility" : 10, "bonus_phisyque" : 20, "must_level" : 10, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное"},
    {"title" : "Кольцо смерти", "bonus_streight" : 50, "bonus_agility" : 15, "bonus_phisyque" : 20, "must_level" : 15, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 480, "rare" : "Легендарное"},
    {"title" : "Клановая печать Теодора", "bonus_streight" : 50, "bonus_agility" : 80, "bonus_phisyque" : 20, "must_level" : 30, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 10000, "rare" : "Реликтовое"},
    {"title" : "Личная печать Теодора", "bonus_streight" : 70, "bonus_agility" : 50, "bonus_phisyque" : 30, "must_level" : 30, "must_streight" : 0, "must_agility" : 0, "must_phisyque" : 0, "attack" : 0, "defend" : 0, "price" : 10000, "rare" : "Реликтовое"},
    {"title" : "Крокодильи сапоги Теодора", "bonus_streight" : 5, "bonus_agility" : 20, "bonus_phisyque" : 0, "must_level" : 30, "must_streight" : 40, "must_agility" : 0, "must_phisyque" : 40, "attack" : 0, "defend" : 30, "price" : 10000, "rare" : "Реликтовое"},
    {"title" : "Хитиновые штаны Теодора", "bonus_streight" : 10, "bonus_agility" : 5, "bonus_phisyque" : 0, "must_level" : 30, "must_streight" : 40, "must_agility" : 0, "must_phisyque" : 40, "attack" : 0, "defend" : 100, "price" : 10000, "rare" : "Реликтовое"},
    {"title" : "Мифриловая куртка Теодора", "bonus_streight" : 5, "bonus_agility" : 25, "bonus_phisyque" : 30, "must_level" : 30, "must_streight" : 40, "must_agility" : 0, "must_phisyque" : 40, "attack" : 0, "defend" : 100, "price" : 10000, "rare" : "Реликтовое"},
    {"title" : "Адамантитовый шлем Теодора", "bonus_streight" : 0, "bonus_agility" : 40, "bonus_phisyque" : 0, "must_level" : 35, "must_streight" : 70, "must_agility" : 0, "must_phisyque" : 60, "attack" : 0, "defend" : 200, "price" : 12000, "rare" : "Реликтовое"},
    {"title" : "Лавовые кинжалы Теодора", "bonus_streight" : 0, "bonus_agility" : 50, "bonus_phisyque" : 0, "must_level" : 40, "must_streight" : 0, "must_agility" : 100, "must_phisyque" : 0, "attack" : 500, "defend" : 0, "price" : 15000, "rare" : "Реликтовое"},
]

def seed_equipments(equipments=EQUIPMENTS, start=0, end=len(EQUIPMENTS)):
    connection = connect("db.db")
    repo = EquipmentRepository(connection)

    for equipment in equipments[start:end]:
        repo.create(**equipment)
        print(f"Предмет {equipment["name"]} создан")
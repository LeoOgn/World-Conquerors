from sqlite3 import connect
from repositories import EquipmentRepository


EQUIPMENTS = [
    {},
]

def seed_equipments(equipments=EQUIPMENTS, start=0, end=len(EQUIPMENTS)):
    connection = connect("db.db")
    repo = EquipmentRepository(connection)

    for equipment in equipments[start:end]:
        repo.create(**equipment)
        print(f"Предмет {equipment["name"]} создан")
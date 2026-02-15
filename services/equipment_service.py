from repositories import InventoryRepository, EquipmentRepository, ItemRepository
from keyboards import NewScores

class EquipmentService:
    def __init__(self, equipment_repo: EquipmentRepository, inventory_repo: InventoryRepository, item_repo: ItemRepository):
        self.equipment_repo = equipment_repo,
        self.inventory_repo = inventory_repo
        self.item_repo = item_repo
    
    def equip(self, character_id: int, item_id: int):
        inventory = self.inventory_repo.get_items_by_character_id(character_id)
        if item_id not in [inv.item_id for inv in inventory]:
            ...
    
    def get_equipment_by_type_id(self, character_id: int, type_id: int):
        inventory = self.inventory_repo.get_items_by_character_id(character_id)
        for inv in inventory:
            item = self.item_repo.get_by_id(inv.item_id)
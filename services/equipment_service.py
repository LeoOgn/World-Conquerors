from repositories import InventoryRepository, EquipmentRepository
from keyboards import NewScores

class EquipmentService:
    def _init_(self, equipment_repo: EquipmentRepository, inventory_repo: InventoryRepository):
        self.equipment_repo = equipment_repo,
        self.inventory_repo = inventory_repo
    
    def equip(self, character_id: int, item_id: int):
        inventory = self.inventory_repo.get_items_by_character_id(character_id)
        if item_id not in [inv.item_id for inv in inventory]:
            ...
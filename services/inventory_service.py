from repositories import InventoryRepository
from typing import List
from repositories import UserInventory, Item, Equipment, ItemRepository


class ItemInfo(Item):
    equipment: Equipment | None = None


class InventoryService:
    def __init__(
        self, 
        inventory_repo: InventoryRepository,
        item_repo: ItemRepository
    ):
        self.inventory_repo = inventory_repo
        self.item_repo = item_repo

    def add_item(self, character_id: int, item_id: int):
        inv = self.inventory_repo.get_inventory_by_item_id(character_id, item_id)
        if inv is None:
            self.inventory_repo.add_item(character_id, item_id)
        else:
            self.inventory_repo.update_item_count(character_id, item_id, inv.count + 1)

    def get_inventory(self, character_id: int) -> List[UserInventory]:
        return self.inventory_repo.get_items_by_character_id(character_id)
        
    def get_item(self, item_id: int) -> ItemInfo:
        item = self.item_repo.get_by_id(item_id)
        if item.equipment_id is not None:
            ...

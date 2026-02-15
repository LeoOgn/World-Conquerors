from handlers import InventoryHandler
from aiogram import Dispatcher, F
from keyboards import InventoryCallback, ItemCallback



class InventoryRouter:
    def __init__(self, dp: Dispatcher, inventory_handler: InventoryHandler):
        self.inventory_handler = inventory_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.callback_query.register(self.inventory_handler.inventory_handler, InventoryCallback.filter())
        self.dp.callback_query.register(self.inventory_handler.item_handler, ItemCallback.filter())
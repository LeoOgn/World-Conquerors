from handlers import LocationHandler
from aiogram import Dispatcher, F



class LocationsRouter:
    def __init__(self, dp: Dispatcher, location_handler: LocationHandler):
        self.location_handler = location_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.location_handler.location_menu, F.text == "Пустоши 🧛🏻")
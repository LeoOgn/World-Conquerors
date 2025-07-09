from handlers import LocationHandler
from aiogram import Dispatcher, F
from keyboards import LocationCallback



class LocationsRouter:
    def __init__(self, dp: Dispatcher, location_handler: LocationHandler):
        self.location_handler = location_handler
        self.dp = dp
        self._setup_routes()

    def _setup_routes(self):
        self.dp.message.register(self.location_handler.location_menu, F.text == "Пустоши 🧛🏻")
        self.dp.callback_query.register(self.location_handler.choose_location, LocationCallback.filter())
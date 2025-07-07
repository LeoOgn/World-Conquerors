from repositories import LocationRepository


class LocationService:
    def __init__(self, location_repo: LocationRepository):
        self.location_repo = location_repo

    def get_all(self):
        return self.location_repo.get_all()
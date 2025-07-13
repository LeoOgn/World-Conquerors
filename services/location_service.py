from repositories import LocationRepository, MobRepository, Mob
from random import randint


class LocationService:
    def __init__(
            self, 
            location_repo: LocationRepository,
            mob_repository: MobRepository
        ):
        self.location_repo = location_repo
        self.mob_repository = mob_repository

    def get_all(self):
        return self.location_repo.get_all()
    
    def get_random_mob(self, location_id: int) -> Mob:
        mobs = self.mob_repository.get_by_location_id(location_id)
        i = randint(0, len(mobs) - 1)
        return mobs[i]
    
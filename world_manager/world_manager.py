import storage_service

class WorldManager(object):

    def __init__(self, storageService):
        self.storageService = storageService

    def get_area(self, region, area):
        """Returns an area"""
        return self.storageService.get_area(region, area)
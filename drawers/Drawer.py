from abc import ABC, abstractmethod


class Drawer(ABC):
    def __init__(self, size, water_level, tile_size):
        self.size = size
        self.water_level = water_level
        self.tile_size = tile_size

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def setWaterLevel(self, water_level):
        self.water_level = water_level

    def getWaterLevel(self):
        return self.water_level

    def setTileSize(self, tile_size):
        self.tile_size = tile_size

    def getTileSize(self):
        return self.tile_size

    @abstractmethod
    def draw(self, screen, field):
        ...

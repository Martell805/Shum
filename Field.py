import numpy


class Field:
    def __init__(self, size, water_level, tile_size, generator, drawer=None):
        self.field = numpy.zeros((size, size))
        self.generator = generator(size)

        if drawer is not None:
            self.drawer = drawer(size, water_level, tile_size)
        else:
            self.drawer = None

    def setSize(self, size):
        self.generator.setSize(size)
        self.drawer.setSize(size)

    def getSize(self):
        return self.generator.getSize()

    def setWaterLevel(self, water_level):
        self.drawer.setWaterLevel(water_level)

    def getWaterLevel(self):
        return self.drawer.getWaterLevel()

    def setTileSize(self, tile_size):
        self.drawer.setTileSize(tile_size)

    def getTileSize(self):
        return self.drawer.getTileSize()

    def __getitem__(self, item):
        return self.field[item]

    def setup(self):
        self.field = self.generator.generate_field()

    def draw(self, screen):
        self.drawer.draw(screen, self)

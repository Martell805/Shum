from .Drawer import Drawer
import pygame


class GB(Drawer):
    def draw(self, screen, field):
        for q, row in enumerate(field):
            for w, cell in enumerate(row):
                if cell > self.getWaterLevel():
                    color = (0, min(max(255 - cell, 0), 255), 0)
                else:
                    color = (0, 0, min(max(255 + cell, 0), 255))

                screen.fill(color, pygame.rect.Rect(q * self.getTileSize(), w * self.getTileSize(),
                                                    self.getTileSize(), self.getTileSize()))

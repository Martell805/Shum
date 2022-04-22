import pygame
from Field import Field
from generators import SinGenerator
from drawers import GB

SIZE = 100
TILE_SIZE = 10
WATER_LEVEL = 0

screen = pygame.display.set_mode((SIZE * TILE_SIZE, SIZE * TILE_SIZE))

field = Field(SIZE, WATER_LEVEL, TILE_SIZE, SinGenerator, GB)
field.setup()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == 32:   # Space
                field.setup()
            elif event.key == 27:   # Esc
                pygame.quit()
                exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print(field[event.pos[0] // TILE_SIZE][event.pos[1] // TILE_SIZE])
            elif event.button == 4:
                field.setWaterLevel(field.getWaterLevel() + 1)
                print(field.getWaterLevel())
            elif event.button == 5:
                field.setWaterLevel(field.getWaterLevel() - 1)
                print(field.getWaterLevel())
            elif event.button == 2:
                field.setWaterLevel(0)
                print(field.getWaterLevel())

    field.draw(screen)

    pygame.display.flip()

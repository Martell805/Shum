from map_working import *
import pygame
from map_generators import *
from drawers import *


# Это программа, которая генерирует карту с 1м вектором


def main(n, m, amp, freq, wl, tilesize):
    # amp = 5, freq = 10, где амплитуда - длинна векторов, частота - расстояние между ними по x и y
    n = n - n % 10
    m = m - m % 10
    screen = pygame.display.set_mode((n * tilesize, m * tilesize))

    my_map, vmas = gen_ov_map(amp, freq, n, m)

    draw_gg(screen, my_map, tilesize)
    draw_vectors(screen, vmas, tilesize)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    my_map, vmas = gen_ov_map(amp, freq, n, m)
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(my_map[event.pos[0] // tilesize][event.pos[1] // tilesize])
        draw_gg(screen, my_map, tilesize)
        draw_vectors(screen, vmas, tilesize)
        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
        n = 20
        m = 20
        amp = 1.3
        freq = 1/5
        wl = 0
        tilesize = 10
        main(n, m, amp, freq, wl, tilesize)

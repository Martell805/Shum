import pygame
from utils.map_working import *
from old_files.perl import gen_perlin_map


TILESIZE = 10


def draw_gg(scr, s):   # Заливает окно серо-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q] > 0:
                scr.fill((0, 255 - s[w][q], 0), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))
            else:
                scr.fill((add_limits(127 + s[w][q][0], 0, 255),
                          add_limits(127 + s[w][q][0], 0, 255),
                          add_limits(127 + s[w][q][0], 0, 255)),
                         pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))


def draw_bgg(scr, s, water_level):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q][1] == -1:
                if s[w][q][0] > 0:
                    scr.fill((0, 255 - s[w][q][0], 0), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))
                else:
                    scr.fill((add_limits(127 + s[w][q][0], 0, 255),
                              add_limits(127 + s[w][q][0], 0, 255),
                              add_limits(127 + s[w][q][0], 0, 255)),
                             pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))
            else:
                scr.fill((0, 0, add_limits((510 - (water_level - s[w][q][0])) // 2, 0, 255)),
                         pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))


def add_normal_water(s, water_level):
    s = add_pairs(s, lambda x: -1)
    for q in range(len(s)):
        if s[q][0][0] <= water_level:
            s[q][0][1] = 0
        if s[q][-1][0] <= water_level:
            s[q][-1][1] = 0
    for q in range(len(s[0])):
        if s[0][q][0] <= water_level:
            s[0][q][1] = 0
        if s[-1][q][0] <= water_level:
            s[-1][q][1] = 0
    k = 0
    flag = True
    while flag:
        flag = False
        for q in range(len(s)):
            for w in range(len(s[0])):
                if s[q][w][1] == k:
                    for dq in (-1, 0, 1):
                        for dw in (-1, 0, 1):
                            if dq != dw and 0 <= q + dq < len(s) and 0 <= w + dw < len(s[0]) and water_level >=\
                                    s[q + dq][w + dw][0] and s[q + dq][w + dw][1] == -1:
                                s[q + dq][w + dw][1] = k + 1
                                flag = True
        k += 1
    return s


def main(n, m, amp, freq, wl):
    # amp = 5, freq = 10, где амплитуда - длинна векторов, частота - расстояние между ними по x и y
    n = n - n % 10
    m = m - m % 10
    screen = pygame.display.set_mode((n * TILESIZE, m * TILESIZE))
    my_map = gen_perlin_map(amp, freq, n, m)
    my_map = add_normal_water(my_map, wl)
    draw_bgg(screen, my_map, wl)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    my_map = gen_perlin_map(amp, freq, n, m)
                    my_map = add_normal_water(my_map, wl)
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(my_map[event.pos[0] // TILESIZE][event.pos[1] // TILESIZE])
        draw_bgg(screen, my_map, wl)
        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
    n = 100
    m = 100
    amp = 1.3
    freq = 1/5
    wl = 0
    main(n, m, amp, freq, wl)

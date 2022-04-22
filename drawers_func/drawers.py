from utils.map_working import *
import pygame


# Тут находятся все функции рисования


def draw_g(scr, s, tilesize):   # Заливает окно серым
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            scr.fill(((255 + s[q][w]) // 2, (255 + s[q][w]) // 2, (255 + s[q][w]) // 2),
                     pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))


def draw_gg(scr, s, tilesize):   # Заливает окно серо-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q] > 0:
                scr.fill((0, 255 - s[w][q], 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
            else:
                scr.fill((add_limits(127 + s[w][q], 0, 255),
                          add_limits(127 + s[w][q], 0, 255),
                          add_limits(127 + s[w][q], 0, 255)),
                         pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))


def draw_bgg(scr, s, water_level, tilesize):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q][1] == -1:
                if s[w][q][0] > 0:
                    scr.fill((0, 255 - s[w][q][0], 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
                else:
                    scr.fill((add_limits(127 + s[w][q][0], 0, 255),
                              add_limits(127 + s[w][q][0], 0, 255),
                              add_limits(127 + s[w][q][0], 0, 255)),
                             pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 - (water_level - s[w][q][0])) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))


def draw_vectors(scr, vmas, tilesize):  # Рисует все векторы
    for q in range(len(vmas)):
        for w in range(len(vmas[0])):
            pygame.draw.circle(scr, (0, 0, 0), (q * 10 * tilesize + tilesize // 2, w * 10 * tilesize + tilesize // 2), 3)
            pygame.draw.line(scr, (0, 0, 0), (q * 10 * tilesize + tilesize // 2, w * 10 * tilesize + tilesize // 2),
                             ((q * 10 + int(vmas[w][q][0])) * tilesize + tilesize // 2,
                              (w * 10 + int(vmas[w][q][1])) * tilesize + tilesize // 2), 3)


def draw_bg_o(scr, s, water_level, tilesize, dx=0, dy=0):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q] > 0:
                scr.fill((0, 255 - s[w][q], 0), pygame.rect.Rect(w * tilesize + dx, q * tilesize + dy,
                                                                 tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 + s[w][q]) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize + dx, q * tilesize + dy, tilesize, tilesize))


def draw_bg(scr, s, water_level, tilesize, dx=0, dy=0):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            cell = add_limits(s[w][q] - water_level, -255, 255)
            if cell > 0:
                scr.fill((0, 255 - cell, 0), pygame.rect.Rect(w * tilesize + dx, q * tilesize + dy,
                                                                 tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 + cell) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize + dx, q * tilesize + dy, tilesize, tilesize))


def draw_bgg_2(scr, s, water_level, tilesize):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q][1] == -1:
                if s[w][q][0] > 0:
                    scr.fill((0, 255 - s[w][q][0], 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
                else:
                    scr.fill((0, 255 + s[w][q][0], 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 - (water_level - s[w][q][0])) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))


def draw_bgg_3(scr, s, water_level, tilesize):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q][1] == -1:
                if s[w][q][0] > 200:
                    scr.fill((s[w][q][0] - 127, s[w][q][0] - 127, s[w][q][0] - 127),
                             pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
                else:
                    scr.fill((0, 255 - s[w][q][0], 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 - (water_level - s[w][q][0])) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))


def draw_bgg_4(scr, s, water_level, tilesize):   # Заливает окно серо-сине-зелёным
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            cell = add_limits(s[w][q][0] - water_level, -255, 255)
            if s[w][q][1] == -1:
                if cell > 200:
                    scr.fill((cell - 127, cell - 127, cell - 127),
                             pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
                else:
                    print((0, 255 - cell, 0))
                    scr.fill((0, 255 - cell, 0), pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))
            else:
                scr.fill((0, 0, add_limits((510 + cell) // 2, 0, 255)),
                         pygame.rect.Rect(w * tilesize, q * tilesize, tilesize, tilesize))

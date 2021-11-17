import random
import pygame
from map_working import *


TILESIZE = 10


def gen_perlin_map(amp, freq, n, m):    # Генерирует массив шума
    n = n - n % 10
    m = m - m % 10
    s = [[0] * n for _ in range(m)]
    vmas = [[(random.random() * 10 - 5, random.random() * 10 - 5) for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]  # Массив векторов
    for q in range(n):  # v1-4 - 4 ближайших к точке вектора
        for w in range(m):
            v1 = vmas[q // 10][w // 10]
            s[q][w] += v1[0] * (q % 10) + v1[1] * (w % 10)
            v2 = vmas[q // 10 + 1][w // 10]
            s[q][w] += v2[0] * (10 - q % 10) + v2[1] * (w % 10)
            v3 = vmas[q // 10][w // 10 + 1]
            s[q][w] += v3[0] * (q % 10) + v3[1] * (10 - w % 10)
            v4 = vmas[q // 10 + 1][w // 10 + 1]
            s[q][w] += v4[0] * (10 - q % 10) + v4[1] * (10 - w % 10)

            s[q][w] = add_limits(s[q][w], -255, 255)
    return s


def draw(scr, s):   # Заливает окно...
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q] > 0:   # ...сине-зелёным
                scr.fill((0, 255 - s[w][q], 0), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))
            else:
                scr.fill((0, 0, 255 + s[w][q]), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))


def draw_vectors(scr, vmas, tilesize):
    for q in range(len(vmas)):
        for w in range(len(vmas[0])):
            pygame.draw.aaline(scr, (0, 0, 0), (q * 10, w * 10),
                               (q * 10 + int(vmas[q][w][0]), w * 10 + int(vmas[q][w][1])))


def main(n, m, amp, freq):
    # amp = 5, freq = 10, где амплитуда - длинна векторов, частота - расстояние между ними по x и y
    n = n - n % 10
    m = m - m % 10
    screen = pygame.display.set_mode((n * TILESIZE, m * TILESIZE))
    my_map = gen_perlin_map(amp, freq, n, m)
    draw(screen, my_map)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    my_map = gen_perlin_map(amp, freq, n, m)
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                my_map = gen_perlin_map(amp, freq, n, m)
        draw(screen, my_map)
        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
    n = 100
    m = 100
    amp = 1.3
    freq = 1/5
    main(n, m, amp, freq)

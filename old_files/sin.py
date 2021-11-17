import math
import random
import pygame


TILESIZE = 10


def gen_sin_map(amp, freq, n, m):
    s = [[0] * n for q in range(m)]

    for q in range(n):
        for w in range(m):
            s[w][q] = int((math.sin((abs(m / 2 - w) + abs(n / 2 - q)) * freq) * amp * random.random() ** 2) * 100)
            if s[w][q] > 255:
                s[w][q] = 255
            if s[w][q] < -255:
                s[w][q] = -255

    return s


def print_map(s):
    for q in s:
        print(*q, sep='\t')


def draw(scr, s):
    scr.fill((0, 0, 0))
    for w in range(len(s)):
        for q in range(len(s[0])):
            if s[w][q] > 0:
                scr.fill((0, abs(255 - s[w][q]), 0), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))
            else:
                scr.fill((0, 0, 255 + s[w][q]), pygame.rect.Rect(w * TILESIZE, q * TILESIZE, TILESIZE, TILESIZE))


def main(n, m, amp, freq):
    screen = pygame.display.set_mode((n * TILESIZE, m * TILESIZE))
    my_map = gen_sin_map(amp, freq, n, m)
    draw(screen, my_map)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:  # Space
                    my_map = gen_sin_map(amp, freq, n, m)
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                my_map = gen_sin_map(amp, freq, n, m)
        draw(screen, my_map)
        pygame.display.flip()


if __name__ == '__main__':
    n = 100
    m = 100
    amp = 1.3
    freq = 1/5
    main(n, m, amp, freq)

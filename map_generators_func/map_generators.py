from utils.map_working import *
import math
import random


# Тут находятся все генераторы и корректоры карт


def gen_sin_map(n, m, amp=1.3, freq=1 / 15, *args):  # Синус
    s = [[0] * n for q in range(m)]

    for q in range(n):
        for w in range(m):
            s[w][q] = int((math.sin((abs(m / 2 - w) + abs(n / 2 - q)) * freq) * amp * random.random() ** 2) * 100)
            if s[w][q] > 255:
                s[w][q] = 255
            if s[w][q] < -255:
                s[w][q] = -255

    return s, []


def gen_perlin_map(n, m, *args):  # Векторное произведение
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[0] * n for _ in range(m)]
    vmas = [[(random.random() * 10 - 5, random.random() * 10 - 5) for _ in range(n // 10 + 1)]
            for _ in range(m // 10 + 1)]
    for q in range(n):
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
    return s, vmas


def add_normal_water(s, water_level, *args):
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
                            if dq != dw and 0 <= q + dq < len(s) and 0 <= w + dw < len(s[0]) and water_level >= \
                                    s[q + dq][w + dw][0] and s[q + dq][w + dw][1] == -1:
                                s[q + dq][w + dw][1] = k + 1
                                flag = True
        k += 1
    return s


def gen_ov_map(n, m, *args):  # Генерирует карту с 1м вектором и кратером на его конце
    # каждая точка - её расстояние до конца вектора
    s = [[0] * n for _ in range(m)]
    vmas = [[(0, 0), (0, 0), (0, 0)],
            [(0, 0), (random.random() * 10 - 5, random.random() * 10 - 5), (0, 0)],
            [(0, 0), (0, 0), (0, 0)]]
    for q in range(n):
        for w in range(m):
            v1 = vmas[1][1]
            s[q][w] = ((q - (10 + v1[0])) ** 2 + (w - (10 + v1[1])) ** 2) ** 0.5
            s[q][w] -= 10
            s[q][w] *= 25
            s[q][w] = add_limits(s[q][w], -255, 255)
    return s, vmas


def gen_len_map(n, m, *args):  # Среднее расстояние до концов 4х ближайших векторов
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[0] * n for _ in range(m)]
    vmas = [[(random.random() * 10 - 5, random.random() * 10 - 5) for _ in range(n // 10 + 1)]
            for _ in range(m // 10 + 1)]
    '''vmas = [[0 for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]  # Генерация векторов одинаковой длины
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 10 - 5
            vmas[q][w] = (xxx, (25 - xxx ** 2) ** 0.5 * random.choice([-1, 1]))'''
    for q in range(n):
        for w in range(m):
            v1 = vmas[q // 10][w // 10]
            s[q][w] += ((q - ((q // 10 * 10) + v1[0])) ** 2 + (w - ((w // 10 * 10) + v1[1])) ** 2) ** 0.5
            v2 = vmas[q // 10 + 1][w // 10]
            s[q][w] += ((q - ((q // 10 * 10 + 10) + v2[0])) ** 2 + (w - ((w // 10 * 10) + v2[1])) ** 2) ** 0.5
            v3 = vmas[q // 10][w // 10 + 1]
            s[q][w] += ((q - ((q // 10 * 10) + v3[0])) ** 2 + (w - ((w // 10 * 10 + 10) + v3[1])) ** 2) ** 0.5
            v4 = vmas[q // 10 + 1][w // 10 + 1]
            s[q][w] += ((q - ((q // 10 * 10 + 10) + v4[0])) ** 2 + (w - ((w // 10 * 10 + 10) + v4[1])) ** 2) ** 0.5
            s[q][w] /= 4
            s[q][w] -= 8.5
            s[q][w] *= -25
            s[q][w] = int(add_limits(s[q][w], -255, 255))
    return s, vmas


def gen_len_map_2(n, m, *args):  # Среднее расстояние до концов всех векторов
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[0] * n for _ in range(m)]
    vmas = [[(random.random() * 20 - 10, random.random() * 20 - 10) for _ in range(n // 10 + 1)]
            for _ in range(m // 10 + 1)]
    for q in range(n):
        for w in range(m):
            for vq in range(n // 10):
                for vw in range(m // 10):
                    v = vmas[vq][vw]
                    s[q][w] += ((q - (vq * 10 + v[0])) ** 2 + (w - (vw * 10 + v[1])) ** 2) ** 0.5
            s[q][w] /= 40
            s[q][w] -= 200
            s[q][w] *= 3.5
            s[q][w] = int(add_limits(s[q][w], -255, 255))
            s[q][w] *= -1
            print(s[q][w])
    return s, vmas


def gen_len_map_3(n, m, *args):  # Среднее расстояние до концов 25и ближайших векторов (квадрат вокруг)
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[0] * n for _ in range(m)]
    vmas = [[(random.random() * 20 - 10, random.random() * 20 - 10) for _ in range(n // 10 + 1)]
            for _ in range(m // 10 + 1)]
    for q in range(n):
        for w in range(m):
            for vq in range(q // 10 - 2, q // 10 + 3):
                for vw in range(w // 10 - 2, w // 10 + 3):
                    try:
                        v = vmas[vq][vw]
                        s[q][w] += ((q - (vq * 10 + v[0])) ** 2 + (w - (vw * 10 + v[1])) ** 2) ** 0.5
                    except Exception:
                        pass
            print(s[q][w])
            s[q][w] /= 40
            s[q][w] **= 2
            s[q][w] = int(add_limits(s[q][w], -255, 255))
            print(s[q][w])
    return s, vmas


def gen_perlin_map_2(n, m, *args):  # Векторное произведение, но все вектора длины 10
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[0] * n for _ in range(m)]
    vmas = [[(0, 0) for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 20 - 10
            vmas[q][w] = (xxx, (100 - xxx ** 2) ** 0.5 * random.choice([-1, 1]))
    for q in range(n):
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
    return s, vmas


def gen_crater_map(n, m, *args):  # Создаёт кратер вокруг конца кажного вектора
    l = 10
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[127] * n for _ in range(m)]

    vmas = [[(0, 0) for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 2 * l - l
            vmas[q][w] = (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))

    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            rad = 10
            c = (q * 10 + vmas[q][w][0], w * 10 + vmas[q][w][1])
            for e in range(c[0] - 10, c[0] + 11):
                for r in range(c[1] - 10, c[1] + 11):
                    try:
                        if distance(c, (e, r)) <= rad:
                            s[e][r] -= 255 / max(0.5, distance(c, (e, r)))
                    except Exception:
                        pass
    for q in range(n):
        for w in range(m):
            s[q][w] = add_limits(s[q][w], -255, 255)
            s[q][w] = int(s[q][w])

    return s, vmas


def gen_crater_map_2(n, m, *args):  # Создаёт кратер вокруг конца кажного вектора x2
    l = 10
    n = n + (10 - n % 10)
    m = m + (10 - m % 10)
    s = [[255] * n for _ in range(m)]

    vmas = [[(0, 0) for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 2 * l - l
            vmas[q][w] = (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))

    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            rad = 10
            c = (q * 10 + vmas[q][w][0], w * 10 + vmas[q][w][1])
            for e in range(c[0] - 10, c[0] + 11):
                for r in range(c[1] - 10, c[1] + 11):
                    try:
                        if distance(c, (e, r)) <= rad:
                            s[e][r] -= 255 / max(0.5, distance(c, (e, r)))
                    except Exception:
                        pass

    vmas = [[(0, 0) for _ in range(n // 10 + 1)] for _ in range(m // 10 + 1)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 2 * l - l
            vmas[q][w] = (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))

    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            rad = 10
            c = (q * 10 + vmas[q][w][0], w * 10 + vmas[q][w][1])
            for e in range(c[0] - 10, c[0] + 11):
                for r in range(c[1] - 10, c[1] + 11):
                    try:
                        if distance(c, (e, r)) <= rad:
                            s[e][r] -= 255 / max(0.5, distance(c, (e, r)))
                    except Exception:
                        pass

    for q in range(n):
        for w in range(m):
            s[q][w] = add_limits(s[q][w], -130, 255)
            s[q][w] = int(s[q][w])

    return s, vmas


def gen_random_map(n, m, *args):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]


def gen_real_perl_map(n, m, *args):
    s = [[-255] * m for _ in range(n)]
    s16 = gen_random_map(n // 16 + 1, m // 16 + 1)
    s8 = gen_random_map(n // 8 + 1, m // 8 + 1)
    s4 = gen_random_map(n // 4 + 1, m // 4 + 1)
    s2 = gen_random_map(n // 2 + 1, m // 2 + 1)
    s1 = gen_random_map(n // 1 + 1, m // 1 + 1)
    for q in range(n):
        for w in range(m):
            s[q][w] += s16[q // 16][w // 16]
            s[q][w] += s8[q // 8][w // 8]
            s[q][w] += s4[q // 4][w // 4]
            s[q][w] += s2[q // 2][w // 2]
            s[q][w] += s1[q // 1][w // 1]
            s[q][w] = add_limits(s[q][w], -255, 255)

    return s, []


def gen_vectors_2(n, m, l):  # Создаёт массив векторов
    vmas = [[(0, 0) for _ in range(n)] for _ in range(m)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 2 * l - l
            vmas[q][w] = (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))
    return vmas


def gen_multy_crater_map(n, m, *args):
    n = n
    m = m
    s = [[800] * n for _ in range(m)]

    for st in range(3, 7):
        vmas = gen_vectors_2(n // 2 ** st + 1, m // 2 ** st + 1, 2 ** st)
        for q in range(len(vmas)):
            for w in range(len(vmas[q])):
                rad = 2 ** st
                c = (q * 2 ** st + vmas[q][w][0], w * 2 ** st + vmas[q][w][1])
                kf = 2 ** (2 * st)
                for e in range(c[0] - 2 ** st, c[0] + 2 ** st + 1):
                    for r in range(c[1] - 2 ** st, c[1] + 2 ** st + 1):
                        try:
                            if distance(c, (e, r)) <= rad:
                                s[e][r] -= kf / max(1, distance(c, (e, r)))
                        except Exception:
                            pass
    for q in range(n):
        for w in range(m):
            s[q][w] *= -1
            s[q][w] *= 0.7
            if s[q][w] > 0:
                s[q][w] *= 0.5
            if s[q][w] > 200:
                s[q][w] = 200 + (s[q][w] - 200) * 0.5

    return s, []

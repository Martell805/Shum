from utils.map_working import *
import random


# Тут находятся все генераторы и корректоры карт, переделанные и сделанные под динамическую генерацию мира


def gen_vmas_crater_map(n, m, vmas):     # Создаёт кратер вокруг конца кажного вектора по массиву векторов vmas
    s = [[127] * n for _ in range(m)]
    for q in range(n // 10):
        for w in range(m // 10):
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

    return s


@njit(fastmath=True)
def gen_vmas_crater_map_fast(n, m, vmas):     # Создаёт кратер вокруг конца каждого вектора по массиву векторов vmas
    # (не работает)
    s = [[127] * n for _ in range(m)]
    for q in range(n // 10):
        for w in range(m // 10):
            rad = 10
            c = (q * 10 + vmas[q][w][0], w * 10 + vmas[q][w][1])
            for e in range(c[0] - 10, c[0] + 11):
                for r in range(c[1] - 10, c[1] + 11):
                    try:
                        if distance_fast(c, (e, r)) <= rad:
                            s[e][r] -= 255 / max(0.5, distance_fast(c, (e, r)))
                    except Exception:
                        pass
    for q in range(n):
        for w in range(m):
            s[q][w] = add_limits_fast(s[q][w], -130, 255)
            s[q][w] = int(s[q][w])

    return s


def gen_vectors(n, m, l):   # Создаёт массив векторов
    vmas = [[(0, 0) for _ in range(n // 10 + 4)] for _ in range(m // 10 + 4)]
    for q in range(len(vmas)):
        for w in range(len(vmas[q])):
            xxx = random.random() * 2 * l - l
            vmas[q][w] = (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))

    return vmas


def add_right_vectors(vmas, l):  # Добавляет столбец векторов справа
    for q in range(len(vmas)):
        xxx = random.random() * 2 * l - l
        vmas[q] += [(int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1])))]

    return vmas


def add_left_vectors(vmas, l):  # Добавляет столбец векторов слева
    for q in range(len(vmas)):
        xxx = random.random() * 2 * l - l
        vmas[q].insert(0, (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1]))))

    return vmas


def add_up_vectors(vmas, l):  # Добавляет строку векторов снизу
    added_v = []
    for q in range(len(vmas[0])):
        xxx = random.random() * 2 * l - l
        added_v.insert(0, (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1]))))
    vmas.insert(0, added_v)

    return vmas


def add_bottom_vectors(vmas, l):  # Добавляет строку векторов сверху
    added_v = []
    for q in range(len(vmas[0])):
        xxx = random.random() * 2 * l - l
        added_v.insert(0, (int(xxx), int((l ** 2 - xxx ** 2) ** 0.5 * random.choice([-1, 1]))))
    vmas += [added_v]

    return vmas


def gen_vmas_crater_map_2(n, m, vmas):     # Создаёт кратер вокруг конца кажного вектора по массиву векторов vmas
    s = [[127] * n for _ in range(m)]
    for q in range(n // 10):
        for w in range(m // 10):
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
            s[q][w] = add_limits(s[q][w], -200, 255)
            s[q][w] = int(s[q][w])

    return s

from numba import njit
# Тут находятся все вспомогательные функции


def print_map(s):
    for q in s:
        print(*q, sep='\t')
    print()


def max_map(s, key=None):
    return max(map(lambda x: max(x, key=key), s), key=key)


def min_map(s, key=None):
    return min(map(lambda x: min(x, key=key), s), key=key)


def add_pairs(s, second=lambda x: 0):
    return list(map(lambda x: list(map(lambda y: [y, second(y)], x)), s))


def add_limits(x, minx, maxx):
    return max(min(x, maxx), minx)


@njit(fastmath=True)
def add_limits_fast(x, minx, maxx):
    return max(min(x, maxx), minx)


def distance(d1, d2):
    return ((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2) ** 0.5


@njit(fastmath=True)
def distance_fast(d1, d2):
    return ((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2) ** 0.5


def slice_map(s, n, m, dx, dy):
    ans = []
    for q in range(dx, n + dx):
        ans.append(s[q][dy:m + dy])
    return ans


def change_pairs(s, second=lambda x: 0):
    return list(map(lambda x: list(map(lambda y: [y[0], second(y[0])], x)), s))
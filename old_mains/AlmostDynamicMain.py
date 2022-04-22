from map_generators_func.dynamic_map_generators import *
from drawers_func.drawers import *

# Это осноная программа (если везде отвечать пустой строкой запустится самая удачная генерация (crater),
# нормальная вода без показа векторов)


MODES = ['', 'crater']
FMODES = [gen_vmas_crater_map, gen_vmas_crater_map]


def main(n, m, amp, freq, wl, tilesize, mode, sv, nw):
    # amp = 5, freq = 10, где амплитуда - длинна векторов, частота - расстояние между ними по x и y
    # (Для всего, кроме сисуса. В синусе амплитуда и частота работают)

    fmode = gen_vmas_crater_map
    try:
        fmode = FMODES[MODES.index(mode)]
    except Exception:
        exit(code='Режим генерации некорректен')

    screen = pygame.display.set_mode((n * tilesize, m * tilesize))
    n = n + 20
    m = m + 20

    dx = 1
    dy = 1

    vmas = gen_vectors(n, m, 10)
    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    vmas = gen_vectors(n, m, 10)
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(my_map[event.pos[0] // tilesize + 10 * dy][event.pos[1] // tilesize + 10 * dx])

        draw_bg(screen, my_map, wl, tilesize)

        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
    m_n = 100
    m_m = 100
    m_amp = 1.3
    m_freq = 1/5
    m_wl = 0
    m_tilesize = 10

    print('Выберите способ построения:')
    print('1. crater   - Создаёт кратер вокруг конца кажного вектора')
    m_mode = 'crater'
    print('crater')

    print('Показвать векторы (Y/N):')
    m_show_vectors = input().lower() != 'n'
    m_normal_water = True

    main(m_n, m_m, m_amp, m_freq, m_wl, m_tilesize, m_mode, m_show_vectors, m_normal_water)

from map_generators_func.map_generators import *
from drawers_func.drawers import *

# Это основная программа (если везде отвечать пустой строкой запустится самая удачная генерация (crater),
# нормальная вода без показа векторов)


MODES = ['', 'sin', 'perl', 'perl-2', 'len-0', 'len', 'len-2', 'len-3', 'crater', 'crater-2', 'perl', 'perl-3',
         'crater-3']
FMODES = [gen_multy_crater_map, gen_sin_map, gen_perlin_map, gen_perlin_map_2,
          gen_ov_map, gen_len_map, gen_len_map_2, gen_len_map_3, gen_crater_map, gen_crater_map_2, gen_real_perl_map,
          gen_multy_crater_map]


def main(n, m, amp, freq, wl, tilesize, mode, sv, nw):
    # amp = 5, freq = 10, где амплитуда - длинна векторов, частота - расстояние между ними по x и y
    # (Для всего, кроме сисуса. В синусе амплитуда и частота работают)

    fmode = gen_crater_map
    try:
        fmode = FMODES[MODES.index(mode)]
    except Exception:
        exit(code='Режим генерации некорректен')

    n = n
    m = m
    screen = pygame.display.set_mode((n * tilesize, m * tilesize))

    my_map, vmas = fmode(n, m, amp, freq)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    my_map, vmas = fmode(n, m, amp, freq)
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(my_map[event.pos[0] // tilesize][event.pos[1] // tilesize])
                elif event.button == 4:
                    wl += 1
                    print(wl)
                elif event.button == 5:
                    wl -= 1
                    print(wl)
                elif event.button == 2:
                    wl = 0
                    print(wl)

        if nw:
            to_draw_map = add_normal_water(my_map, wl)
        else:
            to_draw_map = add_pairs(my_map, lambda x: -1 if x > wl else 1)
        draw_bgg_4(screen, to_draw_map, wl, tilesize)
        if sv:
            draw_vectors(screen, vmas, tilesize)

        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
    m_n = 100
    m_m = 100
    m_amp = 1.3
    m_freq = 1/3
    m_wl = 0
    m_tilesize = 10

    print('Выберите способ построения:')
    print('1. sin      - Синус')
    print('2. perl     - Векторное произведение')
    print('3. perl-2   - Векторное произведение, но все вектора длины 10')
    print('4. len-0    - Генерирует карту с 1м вектором и кратером на его конце '
          '(каждая точка - её расстояние до конца вектора)')
    print('5. len      - Среднее расстояние до концов 4х ближайших векторов')
    print('6. len-2    - Среднее расстояние до концов всех векторов')
    print('7. len-3    - Среднее расстояние до концов 25и ближайших векторов (квадрат вокруг)')
    print('8. crater   - Создаёт кратер вокруг конца кажного вектора')
    print('9. crater-2 - Как crater, но работает дважды')
    print('10. perl-3   - Несколько случайных генераций')
    print('11. crater-3 - Как crater, но с октавами')
    m_mode = input()

    print('Показвать векторы (Y/N):')
    m_show_vectors = input().lower() == 'y'
    print('Генерировать правдоподобную воду (Y/N):')
    m_normal_water = input().lower() == 'y'

    main(m_n, m_m, m_amp, m_freq, m_wl, m_tilesize, m_mode, m_show_vectors, m_normal_water)

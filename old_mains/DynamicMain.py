from map_generators_func.dynamic_map_generators import *
from drawers_func.drawers import *


# Это осноная программа
# (если везде отвечать пустой строкой запустится самая удачная генерация (crater))


MODES = ['', 'crater', 'crater_fast']
FMODES = [gen_vmas_crater_map, gen_vmas_crater_map, gen_vmas_crater_map_fast]


def dynamic_main(n, m, amp, freq, wl, tilesize, mode, sv, nw):
    try:
        fmode = FMODES[MODES.index(mode)]
    except Exception:
        exit(code='Режим генерации некорректен')

    n = n - n % 10
    m = m - m % 10
    screen = pygame.display.set_mode((n * tilesize, m * tilesize))
    n += 2 * 10
    m += 2 * 10

    dx = 1
    dy = 1

    vmas = gen_vectors(n, m, 10)

    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))

    draw_bg(screen, my_map, wl, tilesize)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:  # Space
                    dx = 1
                    dy = 1
                    vmas = gen_vectors(n, m, 5)
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
                elif event.key == 27:  # Esc
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_DOWN:  # V
                    if m // 10 + dy > len(vmas[0]) - 2:
                        vmas = add_right_vectors(vmas, 5)
                        dy += 1
                    else:
                        dy += 1
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
                elif event.key == pygame.K_UP:  # ^
                    if dy < 2:
                        vmas = add_left_vectors(vmas, 5)
                    else:
                        dy -= 1
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
                elif event.key == pygame.K_RIGHT:  # >
                    if n // 10 + dx > len(vmas) - 2:
                        vmas = add_bottom_vectors(vmas, 5)
                        dx += 1
                    else:
                        dx += 1
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
                elif event.key == pygame.K_LEFT:  # <
                    if dx < 2:
                        vmas = add_up_vectors(vmas, 5)
                    else:
                        dx -= 1
                    my_map = fmode(n, m, slice_map(vmas, n // 10, m // 10, dx, dy))
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(my_map[event.pos[0] // tilesize][event.pos[1] // tilesize])
                elif event.button == 4:
                    wl += 1
                elif event.button == 5:
                    wl -= 1
                elif event.button == 2:
                    wl = 0

        draw_bg(screen, my_map, wl, tilesize, -2 * 10, -2 * 10)
        print(wl)
        pygame.display.flip()


if __name__ == '__main__':  # amp и freq ни на что влияют
    m_n = 100
    m_m = 100
    m_amp = 1.3
    m_freq = 1/5
    m_wl = 0
    m_tilesize = 10

    print('Выберите способ построения:')
    print('1. crater - Создаёт кратер вокруг конца кажного вектора')
    print('2. crater_fast - Создаёт кратер вокруг конца кажного вектора, но быстрее (не работает)')
    m_mode = input()

    dynamic_main(m_n, m_m, m_amp, m_freq, m_wl, m_tilesize, m_mode, False, False)

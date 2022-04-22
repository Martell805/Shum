from drawers_func.drawers import *
from map_generators_func.dynamic_map_generators import *


def main():
    n = m = 3 * 10

    screen = pygame.display.set_mode((1, 1))

    dx = 1
    dy = 1

    vmas = gen_vectors(n, m, 5)

    print(dx, dy)
    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == 32:   # Space
                    dx = 1
                    dy = 1
                    vmas = gen_vectors(n, m, 5)
                    print(dx, dy)
                    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')
                elif event.key == 27:   # Esc
                    pygame.quit()
                    exit()
                elif event.key == 275:  # >
                    vmas = add_right_vectors(vmas, 5)
                    dy += 1
                    print(dx, dy)
                    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')
                elif event.key == 276:  # <
                    vmas = add_left_vectors(vmas, 5)

                    print(dx, dy)
                    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')
                elif event.key == 274:  # V
                    vmas = add_bottom_vectors(vmas, 5)
                    dx += 1
                    print(dx, dy)
                    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')
                elif event.key == 273:  # ^
                    vmas = add_up_vectors(vmas, 5)
                    print(dx, dy)
                    print(*slice_map(vmas, n // 10, m // 10, dx, dy), sep='\n')


if __name__ == '__main__':
    main()

from map_working import *
from dynamic_map_generators import *

vmas = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
print(*vmas, sep='\n')
print()

vmas = add_bottom_vectors(vmas, 3)
print(*vmas, sep='\n')
print()

vmas = add_up_vectors(vmas, 3)
print(*vmas, sep='\n')
print()


vmas = add_left_vectors(vmas, 3)
print(*vmas, sep='\n')
print()


vmas = add_right_vectors(vmas, 3)
print(*vmas, sep='\n')
print()


vmas = slice_map(vmas, 3, 3, 1, 1)
print(*vmas, sep='\n')
print()

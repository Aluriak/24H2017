

LAB = """##################
#             #  #
#  #######  # #  #
#  #     ## #
#  # ###    # #  #
#  ### ###### #  #
#             #  #
#  ### #### # #  #
#  # # #  # # #  #
#  # # ## ### #  #
#                #
############### ##
#     #          #
#          #     #
##################
"""


import time
import copy
import itertools
from collections import defaultdict


WORLD = defaultdict(lambda: ' ')
for nol, line in enumerate(LAB.splitlines()):
    if not line: continue
    for idx, c in enumerate(line):
        WORLD[nol, idx] = c
MAX_X = nol
MAX_Y = idx

assert WORLD[1, 1] == ' '
assert WORLD[0, 0] == '#'
assert WORLD[3, 3] == '#'

assert all(v in ' #' for v in WORLD.values())

def test_start(nol, idx, path:str, world, play4human:bool=False) -> bool:
    world = copy.deepcopy(world)
    assert all(p in 'senw' for p in path)
    assert (nol, idx) in world
    cur_x, cur_y = nol, idx
    directions = {'s': (1, 0), 'n': (-1, 0), 'e': (0, 1), 'w': (0, -1)}
    for direction in path:
        if play4human:
            time.sleep(0.01)
        i, j = directions[direction]
        new_x, new_y = cur_x + i, cur_y + j
        if world[new_x, new_y] == ' ':  # ok c'est libre
            if play4human:
                world[cur_x, cur_y] = ' '
            cur_x, cur_y = new_x, new_y
            if play4human:
                world[cur_x, cur_y] = direction
        else:  # un mur !
            pass
        if play4human:
            print_world(world)
    return cur_x, cur_y

def print_world(world):
    assert isinstance(world, defaultdict)
    max_x = max((v[0] for v in world.keys()))
    max_y = max((v[1] for v in world.keys()))
    for i in range(max_x+1):
        for j in range(max_y+1):
            print(world[i, j], end='')
        print()


def is_out(x, y, world) -> bool:
    assert isinstance(world, defaultdict)
    return y >= MAX_Y





if __name__ is '__main__':
    # for line in LAB.splitlines():
        # print(''.join(c if c == '#' else '.' for c in line))

    routine1 = lambda: 2 * 'e' + 2 * 's' + 2 * 'e' + 2 * 's'
    routine = lambda: routine1() + routine1()

    path = (
        routine() + 3 * 'n' + routine() + 3 * 'n' + routine()
        # on recommence !
        # + routine() + 3 * 'n' + routine() + 3 * 'n' + routine()
        # final merge
        + 1 * 'w' + 3 * 's' + routine()
        # go to exit
        + 1 * 'w' + 10 * 'n' + 20 * 'e'
    )

    path = 'nenenenenenenenenenenenenenenenenenenenenenenseeeeeeennneeeeesseeeeeeeeeeeewnnnnnnnnnnnnssee'

    print_world(WORLD)

    print(len(path))
    print(path)
    print('MAXIMUMS:', MAX_X, MAX_Y)
    starts = itertools.product(range(MAX_X), range(MAX_Y))

    for start in starts:
        if WORLD[start] == '#': continue
        last = test_start(*start, path, WORLD)
        if not is_out(*last, WORLD):
            print('!!!:', start, last)
            # test_start(*start, path, WORLD, play4human=True)

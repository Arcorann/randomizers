
# https://tetris.wiki/ARS
# upper left corner of the well is (0, 0)

spawnpos = (4, 1)

pieces = {
    'i': (
        ((-1, -1), (0, -1), (1, -1), (2, -1)),
        ((1, -2), (1, -1), (1, 0), (1, 1)),
    ),
    't': (
        ((-1, -1), (0, -1), (1, -1), (0, 0)),
        ((-1, -1), (0, -2), (0, -1), (0, 0)),
        ((0, -1), (-1, 0), (0, 0), (1, 0)),
        ((0, -2), (0, -1), (0, 0), (1, -1)),
    ),
    'l': (
        ((-1, -1), (0, -1), (1, -1), (-1, 0)),
        ((-1, -2), (0, -2), (0, -1), (0, 0)),
        ((1, -1), (-1, 0), (0, 0), (1, 0)),
        ((0, -2), (0, -1), (0, 0), (1, 0)),
    ),
    'j': (
        ((-1, -1), (0, -1), (1, -1), (1, 0)),
        ((-1, 0), (0, -2), (0, -1), (0, 0)),
        ((-1, -1), (-1, 0), (0, 0), (1, 0)),
        ((0, -2), (0, -1), (0, 0), (1, -2)),
    ),
    's': (
        ((0, -1), (1, -1), (-1, 0), (0, 0)),
        ((-1, -2), (-1, -1), (0, -1), (0, 0)),
    ),
    'z': (
        ((-1, -1), (0, -1), (0, 0), (1, 0)),
        ((1, -2), (1, -1), (0, -1), (0, 0)),
    ),
    'o': (
        ((0, -1), (1, -1), (0, 0), (1, 0)),
    ),
}

colors = {
    'i': (255, 0, 0),
    't': (0, 255, 255),
    'j': (0, 0, 255),
    'l': (255, 127, 0),
    's': (255, 0, 255),
    'z': (0, 255, 0),
    'o': (255, 255, 0),
}

#!/usr/bin/env python
from PIL import Image


MATRIX = [
    [ 1,  0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2],
    [ 3,  4,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   6,   7,   8,   9,  10],
    [11, 12,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  13,  14,  15,  16,  17,  18],
    [19, 20, 21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36],
    [37, 38, 39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54],
    [55, 56, 57,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86],
    [87, 88, 89, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
    [ 0,  0, 58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,   0,   0],
    [ 0,  0, 90,  91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,   0,   0]
]


def join(background, foreground):
    background.paste(foreground, (0, 0), foreground)
    background.show()
    background.save("test3.png")


def concat():
    images = list(map(Image.open, ['data/png/001 copy.png', 'data/png/002 copy.png', 'data/png/003 copy.png']))
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('test.png', format='PNG')


if __name__ == "__main__":
    concat()
    join(Image.open('data/background.jpg'), Image.open('test.png'))
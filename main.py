#!/usr/bin/env python
from PIL import Image


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
    # concat()
    join(Image.open('data/background.jpg'), Image.open('test.png'))
#!/usr/bin/env python
import json

from PIL import Image, ImageDraw, ImageFont

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
    background = background.resize(foreground.size, Image.ANTIALIAS)
    background.paste(foreground, (0, 0), foreground)
    return background


def text(element):
    img = Image.new('RGBA', (1185, 1185))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("data/kaligrafica_allfont_ru.ttf", 170)
    draw.text((0, 0), element['no'], (0, 0, 0), font=font)
    draw.text((800, 0), element['short_name'], (0, 0, 0), font=font)
    draw.text((0, 200), element['electro'], (0, 0, 0), font=font)
    draw.text((0, 400), element['weight'], (0, 0, 0), font=font)
    draw.text((0, 1000), element['latin_name'], (0, 0, 0), font=font)
    draw.text((0, 800), element['russian_name'], (0, 0, 0), font=font)
    img.save('sample-out.png')


def concat(images):

    width, height = images[0][0].size

    total_width = width * len(images[0])
    max_height = height * len(images)

    new_im = Image.new('RGBA', (total_width, max_height))

    y_offset = 0
    for line in images:
        x_offset = 0
        for element in line:
            new_im.paste(element, (x_offset, y_offset))
            x_offset += element.size[0]
        y_offset += line[0].size[1]

    return new_im


def prepare(img):
    bg = Image.new("RGB", (300, 300), (256, 256, 256))  # resize to 300x300
    img = img.resize((300, 300), Image.ANTIALIAS)
    bg.paste(img, img)
    return bg.convert('P', palette=Image.ADAPTIVE, dither=1)


if __name__ == "__main__":
    # images = list(map(prepare, map(Image.open, ('data/png/{0:03d} copy.png'.format(x) for x in range(118)))))
    # gif = Image.new('RGB', (300, 300), (255, 255, 255))
    # gif.save('temp.gif', 'GIF', save_all=True, append_images=images)
    with open('db.json', 'r') as db_file:
        db = json.load(db_file)
        text(db[0])
    # images = [list(map(Image.open, map(lambda x: 'data/png/{0:03d} copy.png'.format(x), MATRIX[i]))) for i in range(len(MATRIX))]
    # concated = concat(images)
    # joined = join(Image.open('data/background.jpg'), concated)
    # joined.save('test.jpg')

import os
from os.path import join, dirname
from PIL import Image, ImageDraw, ImageFont
from string import Template

WIDTH = int(os.environ.get("LABEL_WIDTH"))
HEIGHT = int(os.environ.get("LABEL_HEIGHT"))

OPEN_SANS_REGULAR = [
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 160),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 80),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 70),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 60),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 50),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 40),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 35),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 30),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 20),
    ImageFont.truetype(join(dirname(__file__), 'fonts', 'OpenSans-Regular.ttf'), 10)
]


def select_font(canvas, font_family, text, max_width=WIDTH, max_height=HEIGHT):
    for potential in font_family:
        w, h = canvas.textsize(text, font=potential)
        if w <= WIDTH and w <= max_width and h <= max_height:
            return potential
    return font_family[-1]


def draw_horiz_centered_text(canvas, font_family, y, text, max_width=WIDTH, max_height=HEIGHT):
    font = select_font(canvas, font_family, text, max_width, max_height)
    width, height = canvas.textsize(text, font=font)
    canvas.text(((WIDTH - width)/2, y), text, font=font, fill="black")


def draw_centered_text(canvas, font_family, text, max_height=HEIGHT, fill="black"):
    font = select_font(canvas, font_family, text, max_height=max_height)
    width, height = canvas.multiline_textsize(text, font=font)
    xy = ((WIDTH - width)/2, (HEIGHT - height)/2)
    canvas.multiline_text(xy, text, font=font, fill=fill, align="center", spacing=10)


def create_image(user, raffle=False):
    image = Image.new('L', (WIDTH, HEIGHT), 255)
    canvas = ImageDraw.Draw(image)

    if raffle:
        filename = 'xfair-raffle.png'
        draw_centered_text(canvas, OPEN_SANS_REGULAR, "RAFFLE", fill=180)
    else:
        filename = 'xfair.png'

    draw_horiz_centered_text(canvas, OPEN_SANS_REGULAR, 20, user.name, max_height=HEIGHT/4)

    major_text = '\n'.join([major.strip() for major in user.major.split(',') if major.strip() != ""])
    draw_centered_text(canvas, OPEN_SANS_REGULAR, major_text, max_height=100)

    if user.graduation[0] == "2":
        max_width = 150
    else:
        max_width = 250
    draw_horiz_centered_text(canvas, OPEN_SANS_REGULAR, 280, user.graduation, max_width=max_width)
    draw_horiz_centered_text(canvas, OPEN_SANS_REGULAR, 370, "xFair 2016", max_width=140)

    image.transpose(Image.ROTATE_90).save(join(dirname(__file__), 'labels', filename), "PNG")

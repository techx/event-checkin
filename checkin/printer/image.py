import os
from os.path import join, dirname
from PIL import Image, ImageDraw, ImageFont
from string import Template

from checkin import app

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


def select_font(canvas, font_family, text, max_width, max_height):
    global_width = app.config['LABEL_WIDTH']
    for potential in font_family:
        w, h = canvas.textsize(text, font=potential)
        if w <= global_width and w <= max_width and h <= max_height:
            return potential
    return font_family[-1]


def draw_horiz_centered_text(canvas, font_family, y, text, max_width=None, max_height=None):
    global_width = app.config['LABEL_WIDTH']
    max_width = max_width or app.config['LABEL_WIDTH']
    max_height = max_height or app.config['LABEL_HEIGHT']
    font = select_font(canvas, font_family, text, max_width, max_height)
    width, height = canvas.textsize(text, font=font)
    canvas.text(((global_width - width)/2, y), text, font=font, fill="black")


def draw_centered_text(canvas, font_family, text, max_height, fill="black"):
    max_width = app.config['LABEL_WIDTH']
    global_height = app.config['LABEL_HEIGHT']
    font = select_font(canvas, font_family, text, max_width, max_height=max_height)
    width, height = canvas.multiline_textsize(text, font=font)
    xy = ((max_width - width)/2, (global_height - height)/2)
    canvas.multiline_text(xy, text, font=font, fill=fill, align="center", spacing=10)


def create_image(name, major):
    global_width = app.config['LABEL_WIDTH']
    global_height = app.config['LABEL_HEIGHT']
    image = Image.new('L', (global_width, global_height), 255)
    canvas = ImageDraw.Draw(image)
    filename = 'xfair.png'

    draw_horiz_centered_text(canvas, OPEN_SANS_REGULAR, 20, name, max_height=global_height/4)

    draw_centered_text(canvas, OPEN_SANS_REGULAR, major, max_height=100)

    draw_horiz_centered_text(canvas, OPEN_SANS_REGULAR, 370, "xFair 2017", max_width=140)

    image.transpose(Image.ROTATE_90).save(join(dirname(__file__), 'labels', filename), "PNG")

import image
import os
from os.path import join, dirname

from checkin import app


def print_user(name, major):
    printer = app.config['PRINTER_NAME']
    label = join(dirname(__file__), 'labels', 'xfair.png')
    image.create_image(name, major)
    os.system('lpr -P "{:s}" {:s}'.format(printer, label))

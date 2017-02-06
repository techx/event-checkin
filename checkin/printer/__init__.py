import image
import os
from os.path import join, dirname


def print_user(name, major):
    printer = os.environ.get('PRINTER_NAME')
    label = join(dirname(__file__), 'labels', 'xfair.png')
    image.create_image(name, major)
    os.system('lpr -P "{:s}" {:s}'.format(printer, label))

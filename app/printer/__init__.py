import image
import os
from os.path import join, dirname


def print_user(user):
    printer = os.environ.get('PRINTER_NAME')
    label = join(dirname(__file__), 'labels', 'xfair.png')
    image.create_image(user)
    os.system('lpr -P "{:s}" {:s}'.format(printer, label))
    image.create_image(user, raffle=True)
    os.system('lpr -P "{:s}" {:s}'.format(printer, label))

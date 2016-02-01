import image
import os
from os.path import join, dirname


def print_user(user):
    printer = os.environ.get('PRINTER_NAME')
    raffle_label = join(dirname(__file__), 'labels', 'xfair-raffle.png')
    label = join(dirname(__file__), 'labels', 'xfair.png')
    image.create_image(user, raffle=True)
    os.system('lpr -P "{:s}" {:s}'.format(printer, raffle_label))
    image.create_image(user)
    os.system('lpr -P "{:s}" {:s}'.format(printer, label))

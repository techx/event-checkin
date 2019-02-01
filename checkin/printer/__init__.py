from .image import create_image
import os
from os.path import join, dirname

from checkin import app


def print_user(name, major, year):
    printer = app.config['PRINTER_NAME']
    label = join(dirname(__file__), 'labels', 'xfair.png')
    ipaddress = app.config['IP_ADDRESS']
    create_image(name, major, year)
    # print the tag below based on OS
    if os.name == 'nt':  # windows
        os.system('lpr -S "{:s}" -P {:s} {:s}'.format(ipaddress, printer, label))  # doesn't quite work
    else:  # mac/linux/other
        os.system('lpr -P "{:s}" {:s}'.format(printer, label))

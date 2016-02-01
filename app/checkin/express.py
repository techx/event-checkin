import json
from os.path import join, dirname
import time

from ..model.user import User
from common import prompt, print_xfair_banner

with open(join(dirname(__file__), '..', '..', 'express-data.json')) as json_file:
    users = json.load(json_file)


def checkin_user():
    print_xfair_banner()
    print "Welcome to the express line!"
    mit_id = prompt("Please scan the barcode on the back of your MIT ID")
    if mit_id not in users:
        print "ERROR: Your MIT ID was not found. Please use the regular check-in lines."
        time.sleep(4)
        raise ReferenceError()
    user = users[mit_id]
    result = User()
    result.name = user['name']
    result.email = user['email']
    result.graduation = user['graduation']
    result.major = user['major']
    return result

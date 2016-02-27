from os.path import join, dirname
from dotenv import load_dotenv

import os
import sys
import time

load_dotenv(join(dirname(__file__), '.env'))

if os.environ.get("CHECKIN_TYPE") == "express":
    from app.checkin.express import checkin_user
else:
    from app.checkin.regular import checkin_user

from app.printer import print_user
from app.logger import log_user

if __name__ == "__main__":
    while True:
        try:
            user = checkin_user()

            if user == None: continue
            control_c = False

            print "Printing your name tag and raffle ticket."
            print ""
            print "##########################################################"
            print "PLEASE WAIT FOR BOTH YOUR RAFFLE TICKET AND YOUR NAME TAG."
            print "##########################################################"

            #print_user(user)

            log_user(user)
            time.sleep(5)
        except KeyboardInterrupt:
            time.sleep(0.1)
        except ReferenceError:
            pass

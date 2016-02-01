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
    control_c = False
    while True:
        try:
            user = checkin_user()
            control_c = False
            print "Printing your name tag and raffle ticket..."
            print_user(user)
            log_user(user)
            time.sleep(2)
        except KeyboardInterrupt:
            if control_c == True:
                print "Exiting..."
                sys.exit(0)
            else:
                control_c = True
        except ReferenceError:
            pass

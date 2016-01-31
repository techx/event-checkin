from os.path import join, dirname
from dotenv import load_dotenv

import os

load_dotenv(join(dirname(__file__), '.env'))

if os.environ.get("CHECKIN_TYPE") == "express":
    from app.checkin.express import checkin_user
else:
    from app.checkin.regular import checkin_user

if os.environ.get("OPERATING_SYSTEM") == "windows":
    from app.printer.windows import print_user
else:
    from app.printer.mac import print_user

from app.logger import log_user

if __name__ == "__main__":
    while True:
        user = checkin_user()
        print_user(user)
        log_user(user)

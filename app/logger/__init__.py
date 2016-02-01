from os.path import join, dirname
import datetime

logfile = open(join(dirname(__file__), '..', '..', 'checked-in-emails.log'), 'a')


def log_user(user):
    logfile.write(str(datetime.datetime.utcnow()) + "," + user.email + "\n")
    logfile.flush()

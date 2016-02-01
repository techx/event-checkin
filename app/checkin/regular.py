import os
import requests
import urllib

from ..model.user import User
from common import prompt, print_xfair_banner


def fetch_user(kerberos):
    try:
        response = requests.get(os.environ.get("MIT_API_BASE") + urllib.quote_plus(kerberos))
        if response.status_code == 404:
            print "Sorry, we could not find that kerberos."
            return (None, None, None)
        response.raise_for_status()
        data = response.json()
        default_name = data.get('name', None)
        default_major = data.get('dept', None)
        default_email = kerberos + "@mit.edu"
        return (default_name, default_major, default_email)
    except requests.exceptions.RequestException:
        print "Sorry, an unexpected error occurred."
        return (None, None, None)


def checkin_user():
    print_xfair_banner()
    print "Press enter to accept the default value between the []."
    print "Press Control-C to start over."
    kerberos = prompt("Enter your kerberos")
    default_name, default_major, default_email = fetch_user(kerberos)
    user = User()
    user.name = prompt("Enter your name", default=default_name)
    user.major = prompt("Enter your major(s), comma separated", default=default_major)
    user.graduation = prompt("Enter your graduation year, or 'Graduate' for grad students")
    user.email = prompt("Enter your email", default=default_email)
    return user

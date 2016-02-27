import os
import requests
import urllib

from ..model.user import User
from common import prompt, print_xfair_banner


def fetch_user(email):
    try:
        response = requests.get(
            os.environ.get("REG_API_BASE") + urllib.quote_plus(email),
            timeout=3,
            headers={'x-access-token':os.environ.get("REG_API_JWT")}
        )
        if response.status_code == 404 or response.status_code == 500:
            print "Sorry, we could not find that email."
            return (None, None, None)

        response.raise_for_status()
        data = response.json()

        if not 'profile' in data:
            print("### Did not submit application ###")
            return (None, None, None)

        if not 'admittedDayOne' in data['status'] or not data['status']['admittedDayOne']:
            print("### Not accepted to learnathon ###")

        if not 'admittedDayTwo' in data['status'] or not data['status']['admittedDayTwo']:
            print("### Not accepted to hackathon ###")

        if not 'confirmedDayOne' in data['status'] or not data['status']['confirmedDayOne']:
            print("### Not confirmed to learnathon ###")

        if not 'confirmedDayTwo' in data['status'] or not data['status']['confirmedDayTwo']:
            print("### Not confirmed to hackathon ###")

        default_name = data['profile']['name']
        default_school = data['profile']['school']
        default_grade = data['profile']['grade']
        return (default_name, default_school, default_grade)
    except requests.exceptions.RequestException:
        print "Sorry, an unexpected error occurred."
        return (None, None, None)


def checkin_user():
    print "\nType nothing (and just press enter) to accept the value between the []."
    print "Press Control-C to start over."
    email = prompt("Enter your email")
    default_name, default_school, default_grade = fetch_user(email)

    if default_name == None or default_school == None or default_grade == None:
        return None

    user = User()
    user.email = email
    user.name = prompt("Enter your name", default=default_name)
    user.school = prompt("Enter your high school", default=default_school)
    user.grade = prompt("Enter your email", default=default_grade)
    return user

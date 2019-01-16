import requests
import time
import re
from flask import render_template, url_for, redirect, request, jsonify

from checkin import app
from checkin.printer import print_user

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/custom', methods=['GET'])
def custom():
    return render_template('custom.html')

@app.route('/print', methods=['POST'])
def print_label():
    print_user(request.form['name'], request.form['major'], request.form['year'])
    with open('log.csv', 'a') as f:
        f.write("{},{}\n".format(time.time(), request.form['kerberos']))
    return redirect(url_for('index'))

@app.route('/lookup', methods=['GET'])
def lookup_user():
    r = requests.get('http://jserrino.scripts.mit.edu/lookup/', params={'kerberos': request.args['kerberos']})

    if "There was 1 match to your request." in r.text:
        print(r.text)
        name_search = re.search(r'name: ([^,]+), ([^\n]+)\n', r.text)
        name = name_search.group(2) + ' ' + name_search.group(1)
        year = re.search(r'year: ([^\n+]+)\n', r.text).group(1)
        major = re.search(r'department: ([^\n]+)\n', r.text)

        if year=="1":
            year = "Freshman"
        elif year=="2":
            year = "Sophomore"
        elif year=="3":
            year = "Junior"
        elif year=="4":
            year = "Senior"
        elif year=="G":
            year = "Graduate Student"

        if major is None:
            major = "Undeclared"
        else:
            major = major.group(1)
        return jsonify({
            'major': major,
            'name': name,
            'year': year
        })
    if "No matches to your query." in r.text:
        return jsonify({ 'error': 'No matches were found' }), 404
    return jsonify({ 'error': 'An internal error occured' }), 500

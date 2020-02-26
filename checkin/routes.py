import requests
import time
import re
from flask import render_template, url_for, redirect, request, jsonify

from pymongo import MongoClient;

from checkin import app
from checkin.printer import print_user

from datetime import datetime

client = MongoClient(app.config['MONGO_URI'])

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/custom', methods=['GET'])
def custom():
    return render_template('custom.html')

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/login_data', methods=['GET'])
def get_login_data():
    if (not app.config['DEBUG'] and request.args.get('password') != 'yamatos'):
        return render_template('admin.html', access_denied=True)
    epoch = datetime.utcfromtimestamp(0)
    start_time = request.args.get('start_time')
    if not start_time:
        start_time = 0
    else:
        start_time = (datetime.strptime(start_time, '%Y-%m-%dT%H:%M') - epoch).total_seconds()
    end_time = request.args.get('end_time')
    if not end_time:
        end_time = (datetime.now() - epoch).total_seconds()
    else:
        end_time = (datetime.strptime(end_time, '%Y-%m-%dT%H:%M') - epoch).total_seconds()
    # convert to UTC (assuming we're in Boston)
    start_time += 5*60*60
    end_time += 5*60*60
    db = client['xfair_logins_2019']
    entries = db['entries']
    results = entries.find({'time': {'$lt': end_time, '$gt': start_time}})
    kerbs = set(result['kerberos'] for result in results)
    return render_template('admin.html', got_data=True, num_users=len(kerbs), users=kerbs)

@app.route('/print', methods=['POST'])
def print_label():
    print_user(request.form['name'], request.form['major'], request.form['year'])
    with open('log.csv', 'a') as f:
        f.write("{},{}\n".format(time.time(), request.form['kerberos']))
    db = client['xfair_logins_2019']
    entries = db['entries']
    new_data = {
        'time': time.time(),
        'kerberos': request.form['kerberos']
    }
    entries.insert_one(new_data)
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

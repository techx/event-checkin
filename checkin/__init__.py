from flask import Flask

app = Flask(__name__)

app.config.from_json('../config.json')

import checkin.routes
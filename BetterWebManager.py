import os
import sqlite3

import flask_sijax
from flask import (Flask, escape, g, redirect, render_template, request,
                   session, url_for)

import dataController
#
# Import external files, such as the log and datacontroller
#
# logging [log] - Handles all log based activity
# datacontroller [data] - Handles any database interaction
#
import logMaster

log = logMaster
data = dataController

# Set application name
app = Flask(__name__)
# Set application secret_key and logger
app.secret_key = 'boop'
flask_sijax.Sijax(app)

app.config["SIJAX_STATIC_PATH"] = os.path.join(
    '.', os.path.dirname(__file__), 'static/js/sijax.js')
app.config["SIJAX_JSON_URI"] = '/static/js/json2.js'


@flask_sijax.route(app, "/")
def index():
    return render_template('index.html')


@flask_sijax.route(app, "/login")
def login():
    def check_loginbox(obj_response, userdata, password):
        if (data.checkLogin(userdata, password) == True):
            log.log('Worked')
        obj_response.script('login_error()')

    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('check_loginbox', check_loginbox)
        return g.sijax.process_request()
    return render_template('login.html')


@flask_sijax.route(app, "/signup")
def signup():
    return render_template('signup.html')


@flask_sijax.route(app, "/test")
def test():
    return render_template('test.html')


@flask_sijax.route(app, "/chat")
def chat():
    return render_template('chat.html')


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@flask_sijax.route(app, '/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def Start(PortNumber):
    app.run(host='0.0.0.0', port=PortNumber, debug=False)

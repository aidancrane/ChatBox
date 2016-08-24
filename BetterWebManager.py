#
# Disable flask's logger
#
import logging
import os
import re
import sqlite3

import flask_sijax
from flask import (Flask, escape, g, redirect, render_template, request,
                   session, url_for)

import ConfigManager
import dataController as data
#
# Import external files, such as the log and datacontroller
#
# logging [log] - Handles all log based activity
# datacontroller [data] - Handles any database interaction
#
import logMaster as log
from webfunctions.chat.chat_section import chatPages
from webfunctions.signup.signup_section import signupPages

flasklogger = logging.getLogger('werkzeug')
flasklogger.setLevel(logging.ERROR)


# Set application name
app = Flask(__name__)
# Set application secret_key and logger
app.secret_key = 'boop'
flask_sijax.Sijax(app)

app.config["SIJAX_STATIC_PATH"] = os.path.join(
    '.', os.path.dirname(__file__), 'static/js/sijax.js')
app.config["SIJAX_JSON_URI"] = '/static/js/json2.js'

app.register_blueprint(signupPages)
app.register_blueprint(chatPages)


@flask_sijax.route(app, "/")
def index():
    if 'loggedIn' in session:
        return redirect("/dashboard")
    else:
        return render_template('index.html')


@flask_sijax.route(app, "/login")
def login():
    if 'loggedIn' in session:
        return redirect("/dashboard")
    else:
        def check_loginbox(obj_response, userdata, password):
            if (data.checkLogin(userdata, password) == True):
                populateData = data.userDataPassback(userdata)
                session['userapikey'] = populateData[0]
                session['firstname'] = populateData[1]
                session['lastname'] = populateData[2]
                session['friendlyname'] = populateData[3]
                session['username'] = populateData[4]
                session['emailaddress'] = populateData[5]
                session['loggedIn'] = True
                log.logInfo(
                    "The user '" + populateData[4] + "' logged in via /login and was given user session data")
                obj_response.script('login_success()')
            else:
                obj_response.script('login_error()')

    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('check_loginbox', check_loginbox)
        return g.sijax.process_request()
    return render_template('login.html')


@app.route('/signup')
def signup():
    return redirect(url_for('webfunctions.signup.signup'))


@app.route('/signup/complete')
def signupcomplete():
    return redirect(url_for('webfunctions.signup.signupcomplete'))


@app.route('/chat')
def chat():
    return redirect(url_for('webfunctions.chat'))


@flask_sijax.route(app, "/dashboard")
def dashboard():
    if 'loggedIn' in session:
        return render_template('test.html')
    else:
        return redirect("/")


@flask_sijax.route(app, '/logout')
def logout():
    if 'loggedIn' in session:
        username = session['username']
        session.clear()
        log.logInfo("'" + username + "' logged out via /logout")
        return ("Logged out successfully")
    else:
        return ("You are not logged in silly")


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
    app.run(host='0.0.0.0', port=ConfigManager.Port, debug=True)

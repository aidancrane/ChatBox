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


@flask_sijax.route(app, "/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        firstdata = request.form["username"]
        passdata = request.form["password"]
        if firstdata == "" or passdata == "":
            log.logWarn("A bad password/username combination was used")
            return render_template('index.html', loginfailed="Login Failed!", loginfailedMessage="You need to supply a username and password to login, this can also be your email.")
        else:
            # Check that user cridentials match
            if data.checkLogin(firstdata, passdata) == True:
                # Create server side cookie
                session['loggedIn'] = True
                session['username'] = firstdata
                # Currently No way to determine if user is admin, so they all
                # are
                session['admin'] = True
                # Log event
                log.logInfo(session['username'] +
                            "' logged in successfully")
                return render_template('index.html')
            else:
                return render_template('index.html', loginfailed="Login Failed!", loginfailedMessage="The account you supplied does not exsit, or the password specified was incorrect.")
                log.logWarn("A bad password/username combination was used")
    else:
        return render_template('index.html', head="home")


@flask_sijax.route(app, "/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')

    if request.method == "POST":
        try:
            realName = request.form["inputRealname"]
            username = request.form["inputUsername"]
            email = request.form["inputEmail"]
            emailVerify = request.form["inputEmailSecond"]
            password = request.form["password"]
            passwordVerify = request.form["inputPasswordTwo"]

            if password != passwordVerify:
                return render_template("signup.html", head="admin", redTitle="Oh dears", redBody=", It looks like your passwords did not match, please try again")
            elif email != emailVerify:
                return render_template("signup.html", head="admin", redTitle="Ahh", redBody="It looks like your emails don't match one another, please try again")
            else:
                if realName == "" or username == "":
                    return render_template("signup.html", head="admin", redTitle="This is bad!", redBody="You shouldn't be able to see this, but you left the Name or Screen Name field blank, which is required, so you may have an outdated browser.")
                else:
                    return render_template("signup.html", head="admin", redTitle="Whoo, all is well", redBody="we can start to make your account")
        except:
            log.logError("Signup POST was failed")
            return render_template("signup.html", head="admin", redTitle="Sorry, You cannot make an account at this time", redBody="")


@flask_sijax.route(app, '/database')
def database():
    return (str(data.checkLogin("admin", "password")))


@flask_sijax.route(app, '/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        firstdata = request.form["username"]
        passdata = request.form["password"]
        if request.form["username"] != "" or request.form["password"] != "":
            if data.checkLogin(firstdata, passdata) == True:
                session['loggedin'] = "Yes"
                session['username'] = request.form['username']
            else:
                return render_template('index.html')


@flask_sijax.route(app, '/admin', methods=['GET', 'POST'])
def admin():
    log.logWarm("Admin Panel Accsessed")
    '''
        Needs to check for autethetification!!
    '''
    if request.method == "GET":
        return render_template("/admin/dashboard.html", head="admin")
    if request.method == "POST":
        if request.form['command'] == 'Stop Server':
            log.logInfo("The server was stopped by '" +
                        session['username'] + "'")
            shutdown_server()
            return render_template("/admin/dashboard.html", head="admin",  redTitle="Alert!", redBody="System Shutting down at " + admin.GetTime())
        if request.form['command'] == 'Log Out':
            return redirect(url_for('logout'))

            return render_template("/admin/dashboard.html", head="admin", YellowTitle="You have been Logged out", YellowBody="To login, click the home button")

        if request.form['command'] == 'Remove User':
            username_to_delete = request.form['username_to_delete']
            if username_to_delete == 'admin':
                return render_template("/admin/dashboard.html", head="admin", redTitle="ERROR:", redBody="You cannot delete the 'admin' account.")
            else:
                return render_template("/admin/dashboard.html", head="admin", redTitle="ERROR", redBody="Functionality Incomplete")
        if request.form['command'] == 'Ban User':
            username_to_ban = request.form['username_to_ban']
            if username_to_ban == 'admin':
                return render_template("/admin/dashboard.html", head="admin", redTitle="ERROR:", redBody="You cannot ban the 'admin' account.")
            else:
                return render_template("/admin/dashboard.html", head="admin", redTitle="ERROR", redBody="Functionality Incomplete")

    return render_template("/admin/dashboard.html", head="admin")


@flask_sijax.route(app, '/chat', methods=['GET', 'POST'])
def chat():
    if request.method == "GET":
        return render_template("chat.html", head="chat")

    if request.method == "POST":
        if request.form['push_message_box']:
            push_message = request.form['push_message_box']
            log.logInfo(session['username'] + " > " + push_message)

            return render_template("chat.html", head="chat")
    return render_template("chat.html", head="chat")


@flask_sijax.route(app, '/logout', methods=['GET', 'POST'])
def logout():
    if request.method == "GET":
        username = session['username']
        session.clear()
        log.logInfo("'" + username + "' logged out successfully")
        return render_template("index.html", head="home")


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    log.logInfo("Shutting the Server Down")
    func()
    log.logInfo("Shut down procedure complete")


def Start(PortNumber):
    app.run(host='0.0.0.0', port=PortNumber, debug=False)

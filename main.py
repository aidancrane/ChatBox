from flask import Flask, render_template, redirect, url_for, request, session, escape, request
import os
import sqlite3

#
# Import external files, such as the log and datacontroller
#
# logging [log] - Handles all log based activity
# datacontroller [data] - Handles any database interaction
#
import logMaster
import dataController
log = logMaster
data = dataController

# Set application name
app = Flask(__name__)
# Set application secret_key and logger
app.secret_key = 'boop'



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
         firstdata = request.form["username"]
         passdata = request.form["password"]
         if firstdata == "" or passdata == "":
             log.log("[WARN] A bad password/username combination was used")
             return render_template('index.html', loginfailed="Login Failed!", loginfailedMessage="You need to supply a username and password to login, this can also be your email.")
         else:
             if data.checkLogin(firstdata, passdata) == True:
                 session['loggedin'] = "Yes"
                 session['username'] = firstdata
                 log.log("[INFO] '" + session['username'] + "' logged in successfully")
                 return render_template('index.html')
             else:
                   return render_template('index.html', loginfailed="Login Failed!", loginfailedMessage="The account you supplied does not exsit, or the password specified was incorrect.")
                   log.log("[WARN] A bad password/username combination was used")
    else:
        return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():

     if request.method == 'POST':

          session['username'] = request.form['username']
          session['password'] = request.form['password']

          if 'username' in session:
               if session['username'] != "" or session['password'] != "":
                    return render_template('index.html', isLoggedIn=session['username'])
          return render_template('index.html', type="Sign Up")

     else:
          return render_template('signup.html')

@app.route('/database')
def database():
    return (str(data.checkLogin("admin", "password")))

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/admin/', methods=['GET', 'POST'])
def admin_access():
     username_of_user = session['username']
     logged_in = session['LoggedIn']
     if request.method == "GET":
          if (logged_in == "Yes" and username_of_user in admin.admins):
               return render_template("/admin/dashboard.html")
          else:

               return render_template("index.html")
     elif request.method == "POST":
          pass
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
     if request.method == "GET":
          return render_template("/admin/dashboard.html")
     if request.method == "POST":
          if request.form['command'] == 'Stop Server':
               log.log("[INFO] The server was stopped by '" + session['username'] + "'")
               data.shutdown_server()
               return render_template("/admin/dashboard.html",  redTitle="Alert!", redBody="System Shutting down at " + admin.GetTime())
          if request.form['command'] == 'Log Out':
               if session['username'] or session['password']:
                    username = session['username']
                    del session['username']

               return render_template("/admin/dashboard.html", YellowTitle="You have been Logged out", YellowBody="To login, click the home button")

          if request.form['command'] == 'Remove User':
              username_to_delete = request.form['username_to_delete']
              if username_to_delete == 'admin':
                  return render_template("/admin/dashboard.html", redTitle="ERROR:", redBody="You cannot delete the 'admin' account.")
              else:
                  return render_template("/admin/dashboard.html", redTitle="ERROR", redBody="Functionality Incomplete")
          if request.form['command'] == 'Ban User':
              username_to_ban = request.form['username_to_ban']
              if username_to_ban == 'admin':
                  return render_template("/admin/dashboard.html", redTitle="ERROR:", redBody="You cannot ban the 'admin' account.")
              else:
                  return render_template("/admin/dashboard.html", redTitle="ERROR", redBody="Functionality Incomplete")

     return render_template("/admin/dashboard.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)#setting debug to false allows for printing to the console

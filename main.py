from flask import Flask, render_template, redirect, url_for, request, session, escape, request
#import flask_sijax
import os
app = Flask(__name__)
app.secret_key = 'boop'
import sqlite3
import saveLog
import databaseInteract
admin = saveLog
data = databaseInteract
port = 5000
# Behind the scenes stuff #
import logging
log = logging.getLogger('werkzeug')#logger for flask
log.setLevel(logging.ERROR)#set that only errors are printted to the console


# End of behind the scenes #
admin.init_log()
admin.log("Program Launched")
admin.config()
admin.message_log("~Start of message log~")
admin.log("Loaded config")
print(admin.getAdmins())
print(admin.getBannedIp())
# Front of App #
@app.route("/", methods=['GET', 'POST'])
def index():
     admin.log("[index connction from]" + admin.getIP())
     if request.method == 'POST':
          session['username'] = request.form['username']
          session['password'] = request.form['password']
          if 'username' in session:
               if session['username'] != "" or session['password'] != "":
                    session['loggedin'] = "Yes"
                    if (session['username'] in admin.admins):
                         return render_template("/admin/dashboard.html")
                    return render_template('index.html', isLoggedIn=session['username'])
                    if (session['username'] in admin.admins):
                         return render_template("/admin/dashboard.html")
          return render_template('index.html')

     else:
          return render_template('index.html')
@app.route("/signup", methods=['GET', 'POST'])
def signup():
     admin.log("[signup connction from]" + admin.getIP())
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

     connection = sqlite3.connect("users.db")
     cursor = connection.cursor()
     cursor.execute ("SELECT * FROM Users")
     data = cursor.fetchall()
     for i in data:
          data = i
     #return data[2]
     cursor.close ()
     connection.close()

      #c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn="users", nf="aidan", ft="TEXT"))
@app.route('/login', methods=['GET', 'POST'])
def login():
     return render_template('login.html')
     admin.checkIfIpBanned(getIP())
     error = None
     if request.method == "POST":
          if request.form["username"] != "admin" or request.form["password"] != "admin":
               error = "Invalid cridentials"
          else:
               return redirect(url_for("boop"))
          return render_template("/login.html", error=error)
@app.route('/admin/', methods=['GET', 'POST'])
def admin_access():
     username_of_user = session['username']
     logged_in = session['LoggedIn']
     if request.method == "GET":
          if (logged_in == "Yes" and username_of_user in admin.admins):
               return render_template("/admin/dashboard.html")
          else:
               admin.log("Attempted Acess of admin section by a user with the username: " + session['username'])
               return render_template("index.html")
     elif request.method == "POST":
          pass
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
     if request.method == "GET":
          return render_template("/admin/dashboard.html")
     if request.method == "POST":
          if request.form['kill'] == 'Stop Server':
               admin.shutdown_server()#waits for the last request to be serverd before shutting down
               admin.log("Shutting Down...")
               admin.log("Server Terminated at " + admin.GetTime())
               return render_template("/admin/dashboard.html", isShuttingDown=admin.GetTime())
          if request.form['kill'] == 'Log Out':
               if session['username'] or session['password']:
                    username = session['username']
                    del session['username']
                    del session['password']
                    admin.log("Logging out" + username)

               return render_template("/admin/dashboard.html", isLoggingOut=username)

               #os._exit(1)
               # Do things
     return render_template("/admin/dashboard.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)#setting debug to false allows for printing to the console

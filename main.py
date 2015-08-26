#Test
from flask import Flask, render_template, redirect, url_for, request, session, escape
#import flask_sijax
app = Flask(__name__)
app.secret_key = 'boop'
import sqlite3


@app.route("/", methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          session['email'] = request.form['email']
          session['password'] = request.form['password']

          if 'email' in session:
               if session['email'] != "" or session['password'] != "":
                    return render_template('index.html', isLoggedIn=session['email'])
          return render_template('index.html')

     else:
          return render_template('index.html')
     
@app.route('/database')
def database():
     
     conn = sqlite3.connect("users.db")
     c = conn.cursor()
     c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn="user", nf="aidan", ft="TEXT"))
     return (conn.execute("SELECT aidan  from users"))
     conn.commit()
     conn.close()
     
s
@app.route('/login', methods=['GET', 'POST'])
def login():

     return render_template('login.html')
'''
     error = None
     if request.method == "POST":
          if request.form["username"] != "admin" or request.form["password"] != "admin":
               error = "Invalid cridentials"
          else:
               return redirect(url_for("boop"))
          return render_template("/login.html", error=error)
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

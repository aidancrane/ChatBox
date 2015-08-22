from flask import Flask, render_template, redirect, url_for, request
#import flask_sijax
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          email = request.form['email']
          password = request.form['password']
          return ("POST" + email + password)
     else:
          return render_template('index.html', name="Aidan")


@app.route('/login', methods=['GET', 'POST'])
def login():


     return render_template('login.html', name="Aidan")
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

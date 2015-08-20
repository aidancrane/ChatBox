from flask import Flask, render_template
import flask_sijax
app = Flask(__name__)

@flask_sijax.route(app, "/")
def index():
     return render_template('index.html', name="Aidan")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

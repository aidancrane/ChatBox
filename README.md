# ChatBox
ChatBox is a lightweight Python-built online chat server, It's currently under heavy development but will be ready soon, hopefully. Please, at this time - do not run this in production, the project simply is not ready yet and is not working completly.

Functionality is near-complete but has not been tried and tested compleatly, and a lot of functionaility is not available yet.

## General Requirements

In order to run chatbox you will need

* [Python](https://www.python.org/)
 We are currently developing in Python 3.4.3
* [Flask](http://flask.pocoo.org/)
 Flask is the webserver
* [Flask-Sijax](https://pythonhosted.org/Flask-Sijax/)
 Sijax handles ajax for us
* [Sqlite3](https://www.sqlite.org/)
 Sqlite comes standard with python, so shouldn't need to be installed, we use it to manage our users and (soon) chat logs

## users.db
Currently we are in development so we currently dont have a way of editing users inside of ChatBox, so you will have to use an editing program like [Sqlitebrowser](http://sqlitebrowser.org/).


## Log.log and Message.log
Log.log will contain all verbose information about the server, such as startup and shutdown.
Message.log will contain only messages used by the server.

### Running

To Run the server (currently with 'debug=True', which you should never do publically)

* Install all requirements

	see above

* Start main.py

	python main.py

* You can then browse to [127.0.0.1](http://127.0.0.1/)

In the logfile.log, you should see some logs like so:

        <29-02-2016 22:22:57> [INFO] admin > Test
        <29-02-2016 22:23:01> [INFO] admin > Hello
        <29-02-2016 22:39:55> [INFO] The server was stopped by 'admin'

### Known issues
    Banning an IP is not yet functional
    The chat function does not output to the chat page
    Signing up doesn't add the user to the database
    Banning an IP, removing a user, or banning a user outputs and ERROR: Functionality Incomplete.

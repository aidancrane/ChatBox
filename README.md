# ChatBox
ChatBox is a lightweight Python-built online chat server, It's currently under heavy development but will be ready soon, hopefully.

## General Requirements

In order to run chatbox you will need

* [Python](https://www.python.org/)
 We are currently developing in Python3.4.3
* [Flask](http://flask.pocoo.org/)
 Flask is the webserver and a large part of the server
* [Flask-Sijax](https://pythonhosted.org/Flask-Sijax/)
 (Not currently used, but we will soon)

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

In the Log.log, you should see some logs like so:

	[07-09-2015 12:13:23][Program Launched]; 
	[07-09-2015 12:13:23][Loaded config]; 
	[07-09-2015 12:14:55][[index connction from]127.0.0.1]; 


In the server window, you should see the following:

	[Log] [Program Launched]
	[Log] [Loaded config]
	['admin']
	['']

### Known issues
There is litterally no chat function so far.
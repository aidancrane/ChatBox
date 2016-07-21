import logging
import os
import re
import sqlite3

import flask_sijax
from flask import (Blueprint, Flask, escape, g, redirect, render_template,
                   request, session, url_for)

import ConfigManager
import dataController as data
#
# Import external files, such as the log and datacontroller
#
# logging [log] - Handles all log based activity
# datacontroller [data] - Handles any database interaction
#
import logMaster as log

chatPages = Blueprint('chatblueprint', __name__, template_folder='templates')


@flask_sijax.route(chatPages, "/chat")
def chat():
    if 'loggedIn' in session:
        def parse_input(obj_response, input):
            obj_response.script('input_recorded()')
        if g.sijax.is_sijax_request:
            # Sijax request detected - let Sijax handle it
            g.sijax.register_callback('take_input', parse_input)
            return g.sijax.process_request()
        return render_template('chat.html')
    else:
        return redirect("/")

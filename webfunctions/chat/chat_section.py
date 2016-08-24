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
import webfunctions.chat.chat_parser as chatdata

chatPages = Blueprint('chatblueprint', __name__, template_folder='templates')


@flask_sijax.route(chatPages, "/chat")
def chat():
    if 'loggedIn' in session:
        def parse_input(obj_response, text):
            chatdata.add_messages('UUID', 'displayname', text, 100, 'None')
            obj_response.script('input_recorded()')
        def message_get(obj_response):
            response_text = '<tr id="heldosdfsj"><td><b>displayname ></b> This is a server response</td></tr>'
            obj_response.script("$('tr').last().parent().append('<tr id=\"heldosdfsj\"><td><b>displayname ></b> This is a server response</td></tr>');")
        def update_me(obj_response, lastmessage_id):
            obj_response.script("$('tr').last().append('" + lastmessage_id + "');")
        if g.sijax.is_sijax_request:
            # Sijax request detected - let Sijax handle itHELLO
            g.sijax.register_callback('take_input', parse_input)
            g.sijax.register_callback('get_latest_messages', message_get)
            g.sijax.register_callback('get_latest_update', update_me)
            return g.sijax.process_request()
        return render_template('chat.html', messages = chatdata.get_latest_messages("global"))
    else:
        return redirect("/")

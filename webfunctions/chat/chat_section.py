import logging
import os
import re
from time import gmtime, strftime

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
import webfunctions.chat.chat_commands as chatcoms

chatPages = Blueprint('chatblueprint', __name__, template_folder='templates')


@flask_sijax.route(chatPages, "/chat")
def chat():
    if 'loggedIn' in session:
        def post_message(obj_response, response_text, lastmessage_id):
            obj_response.script("$('tr').last().parent().append('<tr id=\"" + str(lastmessage_id) + "\"><td><b>@server ></b> " + response_text + "</td></tr>');")
            obj_response.script('input_recorded()')
        def update_me(obj_response, lastmessage_id):
            obj_response.script("$('tr').last().parent().append('" + str(chatdata.buildHTMLMessages(lastmessage_id)) + "');")
            obj_response.script("$('#borderedbox').animate({'scrollTop': $('#borderedbox')[0].scrollHeight}, 'slow');")
        def parse_input(obj_response, text, lastmessage_id):
            if chatcoms.check_for_commands(text) != False: #Check if there is a command, sanitisation not needed
                post_message(obj_response, "Hello", chatcoms.sanitize(lastmessage_id))
                obj_response.script("$('#borderedbox').animate({'scrollTop': $('#borderedbox')[0].scrollHeight}, 'slow');")
            elif chatcoms.check_empty(chatcoms.sanitize(text)) == False:
                obj_response.script('input_error()')
            else:
                timeString = strftime("%Y-%m-%d", gmtime())
                timeString = timeString + "@" + strftime("%H:%M:%S", gmtime())
                chatdata.add_messages('UUID', session['username'], chatcoms.sanitize(text), timeString , 'None')
                #strftime("%Y-%m-%d %H:%M:%S", gmtime())
                obj_response.script('input_recorded()')
        if g.sijax.is_sijax_request:
            # Sijax request detected - let Sijax handle itHELLO
            g.sijax.register_callback('take_input', parse_input)
            g.sijax.register_callback('get_latest_update', update_me)
            return g.sijax.process_request()
        return render_template('chat.html', messages = chatdata.get_latest_messages("global"))
    else:
        return redirect("/")

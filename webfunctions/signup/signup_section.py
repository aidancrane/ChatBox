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

signupPages = Blueprint('signupblueprint', __name__,
                        template_folder='templates')


@flask_sijax.route(signupPages, "/signup")
def signup():
    if 'loggedIn' in session:
        return redirect("/")
    else:
        def create_account(obj_response,
                           firstnameinput,
                           lastnameinput,
                           friendlynameinput,
                           usernameinput,
                           emailinput,
                           repeatemailinput,
                           password,
                           repeatedpassword,
                           genderDropdown):
            fail_at_create = False
            if (data.checkIfUserTaken(usernameinput) == True):
                obj_response.script('account_already_taken()')
                fail_at_create = True
            if (data.checkIfUserTaken(emailinput) == True):
                obj_response.script('email_already_taken()')
                fail_at_create = True
            if (firstnameinput == "" or lastnameinput == ""):
                obj_response.script('firstlastnameinput_error()')
                fail_at_create = True
            if friendlynameinput == "":
                obj_response.script('friendlynameinput_error()')
                fail_at_create = True
            if emailinput == "":
                obj_response.script('emailinput_error()')
                fail_at_create = True
            if usernameinput == "":
                obj_response.script('usernameinput_error()')
                fail_at_create = True
            if repeatemailinput == "":
                obj_response.script('repeatemailinput_error()')
                fail_at_create = True
            if password == "":
                obj_response.script('password_error()')
                fail_at_create = True
            if repeatedpassword == "":
                obj_response.script('repeatedpassword_error()')
                fail_at_create = True
            if password != repeatedpassword:
                obj_response.script('password_error()')
                obj_response.script('repeatedpassword_error()')
                obj_response.script('does_not_match()')
                fail_at_create = True
            if emailinput != repeatemailinput:
                obj_response.script('emailinput_error()')
                obj_response.script('repeatemailinput_error()')
                obj_response.script('emails_dont_match()')
                fail_at_create = True
            if usernameinput in open('databases/signup_rules/usernames_banned.txt').read():
                obj_response.script('username_bad()')
                fail_at_create = True

            def allowed_chars_match(strg, search=re.compile(r'[^a-zA-Z0-9.]').search):
                return not bool(search(strg))

            def allowed_chars_match_friendlyname(strg, search=re.compile(r'^[a-zA-Z0-9_ ]*$').search):
                return not bool(search(strg))
            if not allowed_chars_match(usernameinput):
                obj_response.script('usernameinput_error()')
                obj_response.script('username_bad()')
                fail_at_create = True
            if not allowed_chars_match(firstnameinput):
                obj_response.script('name_firendlyname_bad()')
                fail_at_create = True
            if not allowed_chars_match(lastnameinput):
                obj_response.script('name_firendlyname_bad()')
                fail_at_create = True
            if allowed_chars_match_friendlyname(friendlynameinput):
                obj_response.script('name_firendlyname_bad()')
                fail_at_create = True
            if len(password) <= 7:
                obj_response.script('password_too_short()')
                fail_at_create = True
            if password in open('databases/signup_rules/bad_passwords.txt').read():
                obj_response.script('password_too_silly()')
                fail_at_create = True
            if emailinput == repeatemailinput and emailinput != "":
                if not '@' in emailinput:
                    obj_response.script('emailinput_error()')
                    obj_response.script('repeatemailinput_error()')
                    obj_response.script('emails_dont_contain_at()')
                    fail_at_create = True
            if len(firstnameinput) >= 31 or len(lastnameinput) >= 31 or len(friendlynameinput) >= 60 or len(usernameinput) >= 17 or len(emailinput) >= 255 or len(repeatemailinput) >= 255 or len(password) >= 255 or len(repeatedpassword) >= 255 or len(genderDropdown) >= 25:
                obj_response.script('too_long_error()')
                fail_at_create = True
            if fail_at_create == False:
                obj_response.script('create_success()')
                #addUser(firstname, lastname, friendlyname, username, email, password)
                log.logInfo("The user '" + usernameinput +
                            "' was created by /signup. Welcome '" + friendlynameinput + "'.")
                data.addUser(firstnameinput, lastnameinput,
                             friendlynameinput, usernameinput, emailinput, password)
            if fail_at_create == True:
                log.logWarn(
                    "A user attempted to signup at /signup. But did not complete the form correctly.")
                obj_response.script('friendlynameinput_error()')

    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('create_account', create_account)
        return g.sijax.process_request()
    return render_template('signup.html')


@flask_sijax.route(signupPages, "/signup/complete")
def signupcomplete():
    return render_template('signup/signupcomplete.html')

import hashlib
import sqlite3
from random import choice
from string import ascii_lowercase

from flask import request


'''
This is where all the Database Interactions happen.

I will write some docs on this soon.


'''

'''
This is where all the Database Interactions happen.

I will write some docs on this soon.


'''


def buildDatabase():  # Updated July 20 2016
    #
    # Open Database
    #
    opendb()
    #
    # Add Tables with columbs
    #
    cursor.execute('CREATE TABLE `global` (`UUID` TEXT, `displayname` TEXT,`text` TEXT,`timestamp` TEXT,`specialargs` TEXT);')
    #
    # Generate UUID
    #
    combo = "start", "system", "Hello, welcome to chatbox!", '2016',"None"
    cursor.execute(
        "INSERT INTO global VALUES(?,?,?,?,?)", combo)
    connection.commit()
    closedb()

def add_messages(UUID, displayname, text, time, specialargs):  # Updated July 20 2016
    #
    # Open Database
    #
    opendb()
    #
    # Add Tables with columbs
    combo = UUID, displayname, text, time , specialargs
    cursor.execute('INSERT INTO `global`(`UUID`,`displayname`,`text`,`timestamp`,`specialargs`) VALUES (?,?,?,?,?);', combo)
    #
    # Generate UUID
    #
    connection.commit()
    closedb()


def get_latest_messages(channel):  # Updated July 20 2016
    opendb()
    # Check Email and Username for 'data'.
    cursor.execute(
        'SELECT `_rowid_`,* FROM `global` ORDER BY `_rowid_` ASC LIMIT 0, 500')
    uid = cursor.fetchall()
    closedb()
    return uid

def opendb():
    global connection, cursor, connection
    connection = sqlite3.connect("databases/channels/global.db")
    cursor = connection.cursor()
    connection.commit()


def closedb():
    cursor.close()
    connection.close()


for row in get_latest_messages('global'):
    print (row)

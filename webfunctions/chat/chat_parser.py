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
    cursor.execute('CREATE TABLE `global` (`messagenumber` INTEGER, `UUID` TEXT, `displayname` TEXT,`text` TEXT,`timestamp` TEXT,`specialargs` TEXT);')
    #
    # Generate UUID
    #
    combo = "1","start", "system", "Hello, welcome to chatbox!", '2016',"None"
    cursor.execute(
        "INSERT INTO global VALUES(?,?,?,?,?,?)", combo)
    connection.commit()
    closedb()

def getLastMessagenumber():
    opendb()
    cursor.execute('SELECT * FROM  global WHERE   messagenumber = (SELECT MAX(messagenumber)  FROM global);')
    uid = cursor.fetchall()
    connection.commit()
    for row in uid:
        data = row
    return row[0]

def add_messages(UUID, displayname, text, time, specialargs):  # Updated July 20 2016
    #
    # Open Database
    #
    opendb()
    #
    # Add Tables with columbs
    messagenumber = int(getLastMessagenumber()) + 1
    if len(UUID) != 64:
        UUID = (''.join(choice(ascii_lowercase) for i in range(64)))
    combo = messagenumber, UUID, displayname, text, time , specialargs
    cursor.execute('INSERT INTO `global`(`messagenumber`,`UUID`,`displayname`,`text`,`timestamp`,`specialargs`) VALUES (?,?,?,?,?,?);', combo)
    #
    # Generate UUID
    #
    connection.commit()
    closedb()

def buildHTMLMessages(chat_id):
    opendb()
    combo = chat_id
    cursor.execute('SELECT * FROM global WHERE UUID = (?);', [combo])
    uid = cursor.fetchall()
    try:
        for row in uid:
            data = row

        combo = row[0] , getLastMessagenumber()
        cursor.execute('SELECT * FROM global LIMIT ?, ?;', combo)
        uid = cursor.fetchall()
        retbString = ""
        for row in uid:
            retbString = retbString + "<tr id=" + row[1] + "><td><b title=" + row[4] + ">" + row[2] + "></b> " + row[3] + "</td></tr>"
        return retbString
    except:
        return False
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

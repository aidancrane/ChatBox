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
    cursor.execute('CREATE TABLE `users` (`UUID`	TEXT,`apikey`	TEXT,`firstname`	TEXT,`lastname`	INTEGER,`friendlyname`	TEXT,`username`	TEXT,`email`	TEXT,`hashedpassword`	TEXT,`usersalt`	TEXT);')
    #
    # Generate UUID
    #
    UUID = (''.join(choice(ascii_lowercase) for i in range(64)))
    apikey = (''.join(choice(ascii_lowercase) for i in range(64)))
    # Hashed password with static salt, its 'password'
    password = ('982b950c0e958a2c98ee2ae9f53bff3c01586453')
    combo = UUID, apikey, password, 'bwfwxd'
    cursor.execute(
        "INSERT INTO users VALUES(?,?,'admin','admin','Administrator','admin','admin@localhost',? ,?)", combo)
    connection.commit()
    closedb()


def checkLogin(userdata, password):  # Updated July 20 2016
    opendb()
    # Check Email and Username for 'data'.
    detail = (userdata, userdata)
    cursor.execute(
        'SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    for row in uid:
        data = row
    # Check Password Matches
    try:
        if data[7] == checkHashedPassword(userdata, password):
            return True
        else:
            return False
            closedb()
    except:
        return False


def checkHashedPassword(username, password):  # Updated July 20 2016
    opendb()
    # get user salt
    detail = (username, username)
    cursor.execute(
        'SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    for row in uid:
        data = row
    # Check Password Matches
    # print(data)
    Salt = data[8]
    newHash = hashlib.sha1()
    newHash.update(password.encode("utf-8") + Salt.encode("utf-8"))
    return (str(newHash.hexdigest()))


def checkIfUserTaken(username):  # Updated July 20 2016
    opendb()
    # get user salt
    detail = (username, username)
    cursor.execute(
        'SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    for row in uid:
        data = row
    # Check Password Matches
    # print(data)
    if str(uid) == "[]":
        # Username not taken
        return False
    else:
        # taken
        return True


def userDataPassback(username):  # Updated July 20 2016
    opendb()
    # get user salt
    detail = (username, username)
    cursor.execute(
        'SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    for row in uid:
        data = row
    data = list(data)
    # Remove sensitive information
    data.pop(0)
    data.pop(7)
    data.pop(6)
    return (data)


def addUser(realName, userName, Email, password, activeEmail):
    opendb()
    detail = (getLastUUID() + 1, userName, realName,
              Email, hashPassword(password), activeEmail)
    cursor.execute("INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?)", detail)
    connection.commit()
    closedb()


def getPermission(username):
    pass


def getEmailAuth(username):
    pass


def superUser(username):
    pass


def delUser(username):
    pass


def opendb():
    global connection, cursor, connection
    connection = sqlite3.connect("databases/user_data/users.db")
    cursor = connection.cursor()
    connection.commit()


def closedb():
    cursor.close()
    connection.close()

#print (checkLogin("admin", "password"))
# buildDatabase()
#addUser("Aidan Crane", "aidan573", "aidancrane@gmail.com", "passvert", 1)
# printData()
# buildDatabase()
#print(checkHashedPassword('admin', 'passwolrd'))

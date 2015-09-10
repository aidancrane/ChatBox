from flask import request
import sqlite3
import hashlib

def getLastUUID():
    data = cursor.execute('SELECT * FROM Users WHERE UUID = (SELECT MAX(UUID)  FROM Users);')
    uid = cursor.fetchall()
    for row in uid:
          data = row
    return int(data[0])

def buildDatabase():
    cursor.execute('CREATE TABLE Users ( UUID NUMERIC, username TEXT, realname TEXT, email TEXT, password TEXT, active NUMERIC, PRIMARY KEY(UUID));')
    detail = (hashPassword("password"), 1)
    cursor.execute("INSERT INTO Users VALUES(1,'admin','admin','admin@localhost',? ,? )", detail)
    connection.commit()

def checkLogin(data, password):
    #Check Emails
    #Check username
    #Check password matches
    pass

def hashPassword(password):
    Salt = "fishes"
    newHash = hashlib.sha1()
    newHash.update(password.encode("utf-8") + Salt.encode("utf-8"))
    return str(newHash.hexdigest())

def getUser(username):
    pass

def addUser(realName, userName, Email, password, activeEmail):


    detail = (getLastUUID() + 1, userName, realName, Email, hashPassword(password), activeEmail)
    #print ("INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?)", detail)
    cursor.execute("INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?)", detail)
    connection.commit()

def getPermission(username):
    pass

def getEmailAuth(username):
    pass

def superUser(username):
    pass

def delUser(username):
    pass


connection = sqlite3.connect("users.db")
cursor = connection.cursor()
connection.commit()

def closeCursor():
    cursor.close ()
    connection.close()



#buildDatabase()
addUser("Aidan Crane", "aidan573", "aidancrane@gmail.com", "passvert", 1)
#printData()
closeCursor()

from flask import request
import sqlite3

def buildDatabase():
    cursor.execute('CREATE TABLE Users ( UUID NUMERIC, username TEXT, email BLOB, password BLOB, active NUMERIC, PRIMARY KEY(UUID));')
    cursor.execute("INSERT INTO Users VALUES(1,'admin','admin@localhost','password',1)")
    closedb()

def checkLogin(fill, password):
    pass

def hashPassword(password):
    pass

def getUser(username):
    pass

def addUser(realName, userName, Email, password):
    c.execute('CREATE TABLE Users (users aidan)')

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

def closedb():
    cursor.close ()
    connection.close()


buildDatabase()

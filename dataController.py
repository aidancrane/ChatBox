from flask import request
import sqlite3
import hashlib
'''
This is where all the Database Interactions happen.

I will write some docs on this soon.


'''

'''
This is where all the Database Interactions happen.

I will write some docs on this soon.


'''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def getLastUUID():
    opendb()
    data = cursor.execute('SELECT * FROM Users WHERE UUID = (SELECT MAX(UUID)  FROM Users);')
    uid = cursor.fetchall()
    for row in uid:
          data = row
    return int(data[0])
    closedb()

def buildDatabase():
    opendb()
    cursor.execute('CREATE TABLE Users ( UUID NUMERIC, username TEXT, realname TEXT, email TEXT, password TEXT, active NUMERIC, PRIMARY KEY(UUID));')
    detail = (hashPassword("password"), 1)
    cursor.execute("INSERT INTO Users VALUES(1,'admin','admin','admin@localhost',? ,? )", detail)
    connection.commit()
    closedb()

def checkLogin(data, password):
    opendb()
    #Check Email and Username for 'data'.
    detail = (data, data)
    cursor.execute('SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    print (uid)
    for row in uid:
          data = row
    # Check Password Matches
    try:
        if data[4] == hashPassword(password):
            return True
        else:
            return False
            closedb()
    except:
        return False



def hashPassword(password):
    Salt = "fishes"
    newHash = hashlib.sha1()
    newHash.update(password.encode("utf-8") + Salt.encode("utf-8"))
    return str(newHash.hexdigest())

def getUser(getdata):
    opendb()
    #Check Email and Username for 'data'.
    detail = (getdata, getdata)
    cursor.execute('SELECT * FROM Users WHERE email = ? OR username = ?', detail)
    uid = cursor.fetchall()
    print (uid)
    for row in uid:
          data = row
    # Check Password Matches
    if data[4] == hashPassword(password):
        return (uid)
    else:
        return False
    closedb()

def addUser(realName, userName, Email, password, activeEmail):
    opendb()
    detail = (getLastUUID() + 1, userName, realName, Email, hashPassword(password), activeEmail)
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
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    connection.commit()
def closedb():
    cursor.close ()
    connection.close()


#print (checkLogin("admin", "password"))
#buildDatabase()
#addUser("Aidan Crane", "aidan573", "aidancrane@gmail.com", "passvert", 1)
#printData()

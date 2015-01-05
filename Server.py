# THIS IS THE SERVER
# <redacted>

import socket             
import time
import sys
import _thread  
import threading
from threading import Thread
import random
import string
import configparser
import logging
import datetime

def gettime():
    global logtime
    logtime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S" + " : ")
    logging.debug(logtime + "Program was loaded sucessfully")
    
def deleteLogFile():
    # Open the log file
    clearLog = open("log.log", "w")
    clearLog.close()
    
deleteLogFile()
def closeLogFile():
    # This function allows the file to be deleted, after the program has stopped
    clearLog = open("log.log", "r+")
    clearLog.close()
    
def ServerCommands(clientConnection):
    # This is where we check if what we got is private or public
    # for example a password or login
    if sendMessageGlobally == True:
        pushToAll(clientConnection, reply)
        outputConsoleMaster(reply)
    else:
        pushPrivateMessage(clientConnection, reply)
        outputConsoleMaster("PRIVATE: " + reply)

def saveConfig(configName):
    # Save any configuration changes
    with open(configName, "w") as configfile:
        config.write(configfile)
def config():
    global motd
    global config, port
    # create JUST the file if it does not exist or read he file for append, depending on if the file exists
    gereateFileIfNotExist = open("config.cfg","a")
    gereateFileIfNotExist.close()
    #print ("Re-Loading Files")
    # Start config Praser
    config = configparser.ConfigParser()
    config.read("config.cfg")
    # Check if the config exists
    try:
        config.read("config.cfg")
        motd = config.get("Just for fun", "Motd")
        port = config.getint ("Connection details", "port")
    except:
        config.add_section("Just for fun")
        config.set("Just for fun", "Motd", "Default Server - Made by Aidan Crane - Config by Will Smith")
        config.add_section("Connection details")
        config.set("Connection details", "port", "55552")
        saveConfig("config.cfg")
        motd = config.get("Just for fun", "Motd")
        port = config.getint ("Connection details", "port")
config()

def checkGlobalSendall(clientConnection):
    global message
    while True:
        while goGlobalSendall == True:
            if (message != ""):
                try:
                    clientConnection.sendall(bytes(str(message), "utf-8"))
                    logging.basicConfig(filename="log.log",level=logging.INFO)
                    gettime()
                    logging.info(logtime + message)
    
                except OSError:
                    clientConnection.close()
                message = ""

    # Example pushToAll(clientConnection, "Aidan says HI")
def pushToAll(clientConnection, reply):
    global message
    goGlobalSendall = False
    if sendMessageGlobally == True:
        message = reply
    goGlobalSendall = True
    
    # Example pushPrivateMessage(clientConnection, "Your age is 5")
def pushPrivateMessage(clientConnection, message):
    clientConnection.send(bytes(str(message), "utf-8"))

def outputConsoleMaster(output):
    print(str("[Server] " + output))

def parseCommands(clientConnection, recieved):
    if recieved.split()[0][0] == "/":
        pushPrivateMessage(clientConnection, "You did a command! go you!")
    else:
        #pushToAll(clientConnection, "Someones are not Logged in!")
        pushToAll(clientConnection, recieved)

def activeClient(clientConnection):
    global message
    global sendMessageGlobally
   
    clientConnection.send(bytes(str("Hello, you have connected to a test or development server"), "utf-8"))
    clientConnection.send(bytes(str("Here is your random user salt:"), "utf-8"))
    clientConnection.send(bytes(str(''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(5))), "utf-8"))
    clientConnection.send(bytes(str("Enjoy it, it's special, just like Ben!"), "utf-8"))
    clientConnection.send(bytes(str("Before you can talk, you need to login, do /login <username> <password>"), "utf-8"))
    clientConnection.send(bytes(str("Because this is a developer version, or at least the server is, you may be able to talk without a login, go you !"), "utf-8"))
    clientConnection.send(bytes(str("Motd: " + motd), "utf-8"))
    logging.basicConfig(filename="log.log",level=logging.INFO)
    gettime()
    logging.info(logtime + " New Client Message sent")
    
    while True:
        connectionDead = False
        try:
            recieved = clientConnection.recv(1024).decode("utf-8")
        except ConnectionResetError:
            print ("[Server] A Client cut the chord!")
            logging.basicConfig(filename="log.log",level=logging.INFO)
            gettime()
            logging.info(logtime + " A Client cut the chord")
            clientConnection.close()
            connectionDead = True
        except OSError:
            clientConnection.close()
            connectionDead = True
            break

        #Beware : OSError bug lurks here.
        
        reply = (recieved)

        if not recieved:
            break
        if connectionDead == False:
            try:
                sendMessageGlobally = True
                parseCommands(clientConnection, recieved)
                #pushPrivateMessage(clientConnection, reply)
            except ConnectionResetError:
                print ("[Server] + A client has disconnected")
                #clientConnection.close()
                break
        else:
            break
        
    clientConnection.close()

host = '' # Accept all and everything
#port = 55552 this can now be set in the config file if server administrators wish to change the port.

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("[Server] Socket Created Successfully!")

try:
    serverSocket.bind((host, port))
    logging.basicConfig(filename="log.log",level=logging.INFO)
    gettime()
    logging.info(logtime + " Binding...")
except socket.error:
    print ("[Server] Could not bind to port?!!")
    sys.exit()
    logging.basicConfig(filename="log.log",level=logging.INFO)
    gettime()
    logging.info(logtime + " Could not bind to port, please fix this")

print ("[Server] Bind Succesfull!")
logging.basicConfig(filename="log.log",level=logging.INFO)
gettime()
logging.info(logtime + " Binding Successful")
serverSocket.listen(10)

print ("[Server] Listening!")

goGlobalSendall = True
message = ""
#loadlogfile()
while True:
    serverConnection, serverClientAddress = serverSocket.accept()
    print ("[Server] New Connection! " + str(serverClientAddress))
    logging.basicConfig(filename="log.log",level=logging.INFO)
    gettime()
    logging.info(logtime + " New Client Connected from: " + str(serverClientAddress))
    
    _thread.start_new_thread(activeClient ,(serverConnection,))
    _thread.start_new_thread(checkGlobalSendall ,(serverConnection,))

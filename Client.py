# THIS IS THE CLIENT
# <redacted>

import sys
import os
import time
import textwrap
from textwrap import wrap
import socket
import time
import os.path
import logging
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import configparser
import logging
import time
import datetime
import threading
import tkinter.messagebox as message

def restart():
    args = sys.argv[:]
    args.insert(0, sys.executable)
    if sys.platform == 'win32':
        args = ['"%s"' % arg for arg in args]
        
    os.execv(sys.executable, args)

def saveConfig(configName):
    # Save any configuration changes
    with open(configName, "w") as configfile:
        config.write(configfile)

def SaveUserStyle():
    global var
    global UserStyleEntry
    config.read('config.cfg')
    config.set("Client Configuration", "User_Style", (var.get()))
    saveConfig("config.cfg")
    message.showinfo("", "Style Saved")
    
def config():
    global StyleVal
    global Host
    global Port
    global HexVal
   # create the global config
    global config
    # create JUST the file if it does not exist or read he file for append, depending on if the file exists
    gereateFileIfNotExist = open("config.cfg","a")
    gereateFileIfNotExist.close()
    #print ("Re-Loading Files")
    # Start config Praser
    config = configparser.ConfigParser()
    config.read("config.cfg")
    # Check if the config exists
    try:
        config.read('config.cfg')
        HexVal = config.get("Client Configuration", "BGHex_Val")
        StyleVal = config.get("Client Configuration", "Style")
        Run = config.getint("Development", "timesrun")
        Host = config.get("Connection to Server Details", "IP")
        Port = config.get("Connection to Server Details", "Port")
        config.set("Development", "timesrun", str(Run + 1))
        saveConfig("config.cfg")           
    except:
        # Generate config, because it does not exists
        config.add_section("Client Configuration")
        config.add_section("Connection to Server Details")
        config.add_section("Development")
        config.set("Client Configuration", "BGHex_Val", "#FFFDD7")
        HexVal = config.get("Client Configuration", "BGHex_Val")
        config.set("Client Configuration", "Style", "clam")
        StyleVal = config.get("Client Configuration", "Style")
        #config.set("Client Configuration", "Style", "clam")
        config.set("Connection to Server Details", "IP", "127.0.0.1")
        Host = config.get("Connection to Server Details", "IP")
        config.set("Connection to Server Details", "Port", "55552")
        Port = config.get("Connection to Server Details", "Port") 
        config.set("Development", "timesrun", "1")
        saveConfig("config.cfg")
config() 
def saveHexVal():
    global UserHexEntry, hexsettings
    if hexsettings.get() != "":
        config.read('config.cfg')
        config.set("Client Configuration", "BGHex_Val", (hexsettings.get()))
        saveConfig("config.cfg")
        message.showinfo("", "Hex Value Saved")
    elif hexsettings.get() == "":
        message.showerror("ERROR", "Hex Value = null \n Enter A value For Hex")

def loadLogFile():
    global logging
    global logtime
    logtime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S" + " : ")
    logging.basicConfig(filename="log.log",level=logging.DEBUG)
    logging.debug(logtime + "Program was loaded sucessfully")
def deleteLogFile():
    # Open the log file
    clearLog = open("log.log", "w")
    clearLog.close()
    loadLogFile()
def closeLogFile():
    # This function allows the file to be deleted, after the program has stopped
    clearLog = open("log.log", "r+")
    clearLog.close()
def loadItemsInConfig():
    countItemsInFile = sum(1 for line in open("config.cfg"))
    print (str(countItemsInFile))
    #config.get("Slot Names", "user")

def easyPost(noSplitString):

    message = wrap(noSplitString, 90)

    for line in message:
        #print (message)
        outputbox.insert(END, line.rstrip("]")) # .replace(x[:1], '') len(noSplitString)[1:]
    outputbox.update_idletasks()
    outputbox.yview(END)

#def activeServer(serverConnection):
#    clientConnection.send(" Welcome Glorious Leader")
#    
#    while True:
#        
#        recieved = str(serverConnection.recv(1024)).lstrip("b'").rstrip("'")
#        #reply = ("[Server] " + recieved)
#        if not recieved:
#            
#            break
#        #clientConnection.sendall(reply)
#        
#    serverConnection.close()

def pushToServer(message):
    clientSocket.send(bytes(str(message), "utf-8"))

def communcationHandler():
    global clientSocket
    host = config.get("Connection to Server Details", "IP") # Try them all # Run = config.getint("Development", "timesrun")
    port = config.get("Connection to Server Details", "Port")

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("[Client] Socket Created Successfully!")
    print ("[Client] Connecting to '" + str(host) + "' on port #" + port)

    try:
        clientSocket.connect((str(host), int(port)))
    except ConnectionRefusedError:
        print ("[Client] Connection Failed")
        easyPost ("[Client] Server not online?!")
        sys.exit()

    #clientSocket.send(bytes(str("Hallo from Client"), "utf-8"))
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        easyPost(("[From Server]" + data.decode("utf-8")))

def userPushToServer(event=None):
    global entrybox 
    message = entrybox.get()
    if message != "":
        pushToServer(message)
        entrybox.delete(0,END)

def graphicalInterfaceSetUp():
    global swingWindow
    global outputbox
    global entrybox
    global HexVal
    global Title
    swingWindow = Tk()
    # look at this, this was written by jaidon, beware. It is truely awful coding.
    s = ttk.Style()
    s.theme_use(StyleVal)
    swingWindow.title("ChatBox™")
    swingWindow.geometry("478x485")
    swingWindow.resizable(0,0)
    swingWindow.configure(background=HexVal)
    swingWindow.wm_iconbitmap('icon.ico')
    scrollbar = Scrollbar(swingWindow)# wrap=WORD) # Aidan added wrap=WORD
    scrollbar.grid(column=2, row=1, sticky=NS)
    #windowwidth="470px"
    Title = Label(swingWindow, text="Group Chat", background=HexVal, font=("Calibri", 16))
    Title.grid(row=0, column=0, sticky=W)
    Cog = PhotoImage(file="cog.gif")
    Settingsbtn = Button(swingWindow, image=Cog, command=Settings)
    Settingsbtn.grid(row=0, column=1, columnspan=2, sticky=E)
    outputbox = Listbox(swingWindow, yscrollcommand=scrollbar.set, height='26', width='76')
    outputbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx='2', pady='2')
    scrollbar.config(command=outputbox.yview)
    entrybox = Entry(swingWindow, width='65')
    entrybox.grid(row=2, column=0, sticky=NSEW)
    send = Button(swingWindow, text='Send', command=userPushToServer)
    send.grid(row=2, column=1, columnspan=2, sticky=NSEW)
    swingWindow.bind('<Return>', userPushToServer)
    swingWindow.mainloop()

def gText(String): # The def that could'nt, love aidan
    Title.labelText = String

def UserUI():   
    saveHexVal()
    SaveUserStyle()
        
def UserIPIncoming():
    global stylesettings
    global incomingIP
    global incomingPort
    global UserIPIncomingEntry
    global UserPortIncomingEntry
    UserIPIncomingEntry = incomingIP.get()
    UserPortIncomingEntry = incomingPort.get()
    config.read('config.cfg')
    config.set("Connection to Server Details", "IP", UserIPIncomingEntry)
    config.set("Connection to Server Details", "Port", UserPortIncomingEntry)
    saveConfig("config.cfg")
    message.showinfo("", "IP and Port Saved")
     
        
def Settings(): 
    global SettingsWindow, hexsettings, HexVal, stylesettings, var, Host, Port
    global incomingIP
    global incomingPort
    SettingsWindow = Tk()
    var = ""
    s2 = ttk.Style()
    s2.theme_use(StyleVal)
    SettingsWindow.title("ChatBox™ Settings")
    SettingsWindow.geometry("360x240")
    SettingsWindow.resizable(0,0)
    SettingsWindow.wm_iconbitmap('icon.ico')
    SettingsWindow.configure(background=HexVal)
    settingsTitle = Label(SettingsWindow, text="ChatBox™ Settings", background=HexVal, font=("Calibri", 16))
    settingsTitle.grid(row=0, column=0, sticky=NSEW, columnspan=2)
    hexsettingsTitle = Label(SettingsWindow, text='Set the background colour (use a hex code):', background=HexVal, width='43')
    hexsettingsTitle.grid(row=1, column=0, sticky=NSEW, columnspan=2)
    hexsettings = Entry(SettingsWindow, width='5', background=HexVal)
    hexsettings.grid(row=2, column=0, sticky=NSEW)
    hexsettings.insert(0, HexVal)
    var = StringVar(SettingsWindow)
    var.set(StyleVal)
    options = ['clam', 'clam', 'alt', 'xpnative', 'winnative', 'vista',]
    stylesettings = OptionMenu(SettingsWindow, var, *options)
    stylesettings.grid(row=2, column=1, sticky=NSEW)
    uisettingsSend = Button(SettingsWindow, text='Set', command=UserUI)
    uisettingsSend.grid(row=2, column=2, sticky=NSEW)
    incomingIPTitle = Label(SettingsWindow, text='Set the incoming IP address and port:', background=HexVal, width='10')
    incomingIPTitle.grid(row=3, column=0, sticky=NSEW, columnspan=2)
    incomingIP = Entry(SettingsWindow, width='5', background=HexVal)
    incomingIP.insert(0, Host)
    incomingIP.grid(row=4, column=0, sticky=NSEW)
    incomingPort = Entry(SettingsWindow, width='5')
    incomingPort.insert(0, Port)
    incomingPort.grid(row=4, column=1, sticky=NSEW)
    incomingIPSend = Button(SettingsWindow, text='Set', command=UserIPIncoming)  
    incomingIPSend.grid(row=4, column=2, sticky=NSEW)
    Apply = Button(SettingsWindow, text='Apply', command=restart)
    Apply.grid(row=5, column=0, sticky=NSEW)
    SettingsWindow.mainloop()

communcationHandlerThread = threading.Thread(name='communcationHandler', target=communcationHandler)
graphicalThread = threading.Thread(name='graphicalInterfaceSetUp', target=graphicalInterfaceSetUp)
graphicalThread.start()
time.sleep(1)
communcationHandlerThread.start()

communcationHandlerThread.join()
graphicalThread.join()

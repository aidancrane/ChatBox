# Logfile
#
# This is where all logging goes through
#
#
#
import datetime

def getTime():
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return time

def log(log_message):
     print ("[Log] [" + log_message + "]")
     log = open("logfile.log", 'a')
     log.write("<" + getTime() + "> " + log_message + "\n")
     log.close()

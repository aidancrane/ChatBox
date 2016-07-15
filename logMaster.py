# Logfile
#
# This is where all logging goes through

import datetime


'''
    Log Format:
    "[Time][Type][Message]"
'''
def init():
    log = open("logfile.log", 'w')
    log.close()

def getTime():
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return time

def logInfo(log_message):
    log_msg_final = "[" + getTime() + "] [INFO] [" + log_message + "]"
    print("\033[92m" + log_msg_final + "\033[0m")
    log(log_msg_final)

def logError(log_message):
    log_msg_final = "[" + getTime() + "] [Error] [" + log_message + "]"
    print("\033[91m" + log_msg_final + "\033[0m")
    log(log_msg_final)

def logWarn(log_message):
    log_msg_final = "[" + getTime() + "] [Warn] [" + log_message + "]"
    print("\033[93m" + log_msg_final + "\033[0m")
    log(log_msg_final)

def log(log_message):
    ### Depreciated, Should not be used in the program, please use the above log types
    log = open("logfile.log", 'a')
    log.write("[" + getTime() + "][" + log_message + "]\n")
    log.close()

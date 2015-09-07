from flask import request
import datetime
import configparser
admins = []
bannedIps = []
config_file = "config.cfg"
def getAdmins():
    config.read(config_file)
    adminspresplit = config.get("Settings", "Admins")
    admins = list(adminspresplit.split(','))
    return admins
def getBannedIp():
    bannedIpsprelist = config.get("Bans", "Banned Ips")
    bannedIps = list(bannedIpsprelist.split(','))
    return bannedIps
def saveConfig(configName):
    # Save any configuration changes
    with open(configName, "w") as configfile:
        config.write(configfile)
def config():
     # create the global config
     global config, log_user_messages, console_user_messages, port, num_of_bans, admins, bannedIps
     # create JUST the file if it does not exist or read he file for append, depending on if the file exists
     gereateFileIfNotExist = open(config_file,"a")
     gereateFileIfNotExist.close()
     config = configparser.ConfigParser()
     config.read(config_file)
     # Check if the config exists
     try:
         config.read(config_file)
         shall_we_log = config.get("Settings", "Log User Messages").lower()
         shall_print_to_console = config.get("Settings", "Print Messages to Console").lower()
         adminspresplit = config.get("Settings", "Admins")
         admins = list(adminspresplit.split(','))
         bannedIpsprelist = config.get("Bans", "Banned Ips")
         bannedIps = list(bannedIpsprelist.split(','))
         try:
             port = config.getint("Settings", "Port")
         except ValueError:
             port = 5000
             log("Port Value error, port set to: " + port)
         saveConfig(config_file)           
     except:
         # Generate config, because it does not exists
         config.read(config_file)
         #clear_file = open("config.cfg", 'w')
         #clear_file.close()
         config.add_section("Settings")
         config.set("Settings", "Log User Messages", "true")
         config.set("Settings", "Print Messages to Console", "false")
         config.set("Settings", "Admins", "admin")
         config.set("Settings", "Port", "5000")
         config.add_section("Bans")
         config.set("Bans", "Banned Ips", "")
         saveConfig(config_file)
         shall_we_log = config.get("Settings", "Log User Messages").lower()
         shall_print_to_console = config.get("Settings", "Print Messages to Console").lower()   
     if (shall_we_log == "true"):
          log_user_messages = True
     else:
          log_user_message = False
     if (shall_print_to_console == "true"):
          console_user_messages = True
     else:
          console_user_messages = False
def init_log():
     #Clears all logs when program first runs.
     log_file = open("Log.log", 'w')
     log_file.close()
     message_file = open("Message_log.log", 'w')
     message_file.close()
     
def log(log_message):
     timeOfLog = GetTime()
     print ("[Log] [" + log_message + "]")
     log = open("Log.log", 'a')
     #Add username logging here when usernames are sorted.
     log.write("[" + timeOfLog + "][" + log_message + "]; \n")
     log.close()

def GetTime():
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return time
def message_log(log_message):
     if (log_user_messages):
          timeOfLog = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
          if (console_user_messages):
               print ("[MSG] [" + log_message + "]")
          message_log = open("Message_Log.log", 'a')
          #Add username logging here when usernames are sorted.
          message_log.write("[" + timeOfLog + "]:[" + log_message + "]; \n")
          message_log.close()
def getIP():
    ip = request.headers.get('User-Agent')
    user_ip = str(request.remote_addr)
    return user_ip
def checkIfIpBanned(ip):
    if (ip in bannedIps):
        return render_template('banned.html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

import configparser, logMaster
config = configparser.ConfigParser()
configFileName = "config.cfg"

Port=""
Font=""
def init():
    gereateFileIfNotExist = open(configFileName,"a")
    gereateFileIfNotExist.close()
    config.read(configFileName)
    CheckVariables()

def CheckVariables():
    global Port, Font
    Port=getPort()
    Font=getFont()
def getPort():
    while True:
        try:
            theport = config.getint("Web Settings", "Port")
            break
        except configparser.NoSectionError:#If the section "web settings" does not exsist it creates it
            logMaster.logWarn("The Config Section, 'Web Settings', could not be found")
            config.add_section("Web Settings")
            saveConfig(configFileName)
            logMaster.logInfo("The Config Section, 'Web Settings', has been created")
        except configparser.NoOptionError:#if the option "port" does not exsist, it creates it
            logMaster.logWarn("The Config Option, 'Port', could not be found")
            config.set("Web Settings", "Port", "8888")
            saveConfig(configFileName)
            logMaster.logInfo("The Config Option, 'Port', has been created")
    return theport

def getFont():
    while True:
        try:
            thefont = config.get("Display Settings", "Font")
            break
        except configparser.NoSectionError:#If the section "web settings" does not exsist it creates it
            logMaster.logWarn("The Config Section, 'Display Settings', could not be found")
            config.add_section("Display Settings")
            saveConfig(configFileName)
            logMaster.logInfo("The Config Section, 'Display Settings', has been created")
        except configparser.NoOptionError:#if the option "port" does not exsist, it creates it
            logMaster.logWarn("The Config Option, 'Font', could not be found")
            config.set("Display Settings", "Font", '"sans serif"')
            saveConfig(configFileName)
            logMaster.logInfo("The Config Option, 'Font', has been created")
    return thefont
def saveConfig(configName):
    # Save any configuration changes
    with open(configName, "w") as configfile:
        config.write(configfile)

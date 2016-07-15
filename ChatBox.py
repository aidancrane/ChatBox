import WebManager, logMaster, ConfigManager



def Start():
    ConfigManager.init()
    logMaster.init()

    logMaster.log("About to Start Chatbox on the port: " +str(ConfigManager.Port))
    WebManager.Start(ConfigManager.Port)
    logMaster.log("Server Closed")

print("Started at: ", logMaster.getTime())
Start()

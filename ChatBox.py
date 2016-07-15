import WebManager, logMaster, ConfigManager



def Start():
    ConfigManager.init()
    portNum=ConfigManager.Port
    logMaster.init()
    logMaster.log("About to Start Chatbox on the port: " +str(portNum))
    WebManager.Start(portNum)
    logMaster.log("Server Closed")

Start()

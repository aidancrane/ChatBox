import ConfigManager
import logMaster
import WebManager


def Start():
    ConfigManager.init()
    logMaster.init()

    logMaster.logInfo(
        "About to Start Chatbox Server on the port: " + str(ConfigManager.Port))
    WebManager.Start(ConfigManager.Port)
    logMaster.log("Server Closed")

logMaster.logInfo("Starting ChatBox")
Start()

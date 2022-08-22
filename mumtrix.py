import pymumble_py3 as pymumble
import time
import requests
import sys
import os
from configparser import ConfigParser

"""
Connects to a Mumble server and sends current user count to a Matrix room.
"""

__version__ = "0.4.0"
DRY_RUN = False


def get_config(config_path="./mumtrix.ini"):
    """
    DO NOT EDIT this config text below, edit the mumtrix.ini instead!
    """
    config = ConfigParser(allow_no_value=True)
    config.optionxform = str

    if os.path.isfile(config_path):
        config.read(config_path)
        return config

    else:
        config["General"] = {
                "BotName": "MumtrixBot"
                }

        config["Mumble"] = {
                "Host": "example.org",
                "Port": "64738",
                "; You can obtain the channel id (assuming you have the rights) by rightclicking on the channel > Edit… > Properties Tab and then you can see it to the right side of the channel name (ID: ####)": None,
                "JoinChannelID": "",
                "CertFilePath": "./mumble_certfile.pem",
                "KeyFilePath": "./mumble_keyfile.pem",
                "; for option BotComment at least two spaces are needed before every new line (multiline support)": None,
                "BotComment": """
<h2>Hola, I'm Mumtrix :)</h2><br />
I post the number of currently connected users - on this Mumble server – to Matrix.""",
                "; Check interval in seconds": None,
                "CheckInterval": "5", 
                "DebugPymumble": "False"
                }

        config["Matrix"] = {
                "; Protocol options: http or https": None,
                "Protocol": "https",
                "Host": "example.org",
                "Port": "4785",
                "; Full room id is needed (including the \"!\")": None,
                "JoinRoomID": "!example:example.org",
                "; Insert user count with {currentUserCount}": None,
                "CurrentUserCountMessageEmpty": "At the moment there is no user on Mumble.",
                "CurrentUserCountMessageSingular": "At the moment there is one user on Mumble.",
                "CurrentUserCountMessagePlural": "At the moment there are {currentUserCount} users on Mumble.",
                "; You can get the api key from the matrix webhook config": None,
                "ApiKey": ""
                }

        with open(config_path, 'w') as configfile:
            config.write(configfile)

        print("Please edit the config file just created at '" + config_path + "' and make sure to change all required options.")
        print("For more information consult the README.")
        sys.exit(1)


def getNumerus(objectCount):
    if objectCount == 0:
        return "Empty"
    elif objectCount == 1:
        return "Singular"
    elif objectCount > 1:
        return "Plural"
    else:
        print("The object count is not valid.")
        sys.exit(1)


def generateMatrixMessage(cfg, currentUserCount):
    currentUserCount -= 1
    currentUserCountMessageNumerus = "CurrentUserCountMessage" + getNumerus(currentUserCount)

    return {
        "body": cfg["Matrix"][currentUserCountMessageNumerus].format(currentUserCount=str(currentUserCount)),
        "key": cfg["Matrix"]["ApiKey"]
    }


def removeFirstNewline(text):
    """
    remove one leading new line
    """
    if text.strip() and text[0] == "\n":
        return text[1:]
    else:
        return text


def setupMumbleBot(cfg):
    bot = pymumble.Mumble(cfg["Mumble"]["Host"],
                          cfg["General"]["BotName"],
                          port=cfg["Mumble"].getint("Port"),
                          certfile=cfg["Mumble"]["CertFilePath"],
                          keyfile=cfg["Mumble"]["KeyFilePath"],
                          debug=cfg["Mumble"].getboolean("DebugPymumble"))

    bot.set_application_string("Mumtrix - " + __version__)
    bot.start()
    bot.is_ready()

    bot.users.myself.comment(removeFirstNewline(cfg["Mumble"]["BotComment"]))
    bot.users.myself.deafen()
    bot.channels[cfg["Mumble"].getint("JoinChannelID")].move_in()
    return bot


def main():
    #cfg = get_config("./mumtrix_dev.ini")
    cfg = get_config()
    bot = setupMumbleBot(cfg)

    MatrixURL = cfg["Matrix"]["Protocol"] + "://" + cfg["Matrix"]["Host"] + ":" + cfg["Matrix"]["Port"] + "/" + cfg["Matrix"]["JoinRoomID"]

    try:
        first_message = True
        lastUserCount = 0
        while True:
            currentUserCount = bot.users.count()
            print(currentUserCount)
            if not first_message and currentUserCount != lastUserCount:
                print("User count: " + str(currentUserCount - 1))
                if not DRY_RUN:
                    print("Posting to Matrix.")
                    requests.post(MatrixURL, json=generateMatrixMessage(cfg, currentUserCount))
            elif first_message:
                print("First message skipped.")

            else:
                print("User count did not change.")

            time.sleep(cfg["Mumble"].getint("CheckInterval"))
            first_message = False
            lastUserCount = currentUserCount

    except KeyboardInterrupt:
        print("User interrupted.", __file__)

if __name__ == "__main__":
    main()

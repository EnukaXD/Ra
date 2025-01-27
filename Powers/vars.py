from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="1517994352 1344569458 1432756163 1874070588 1355478165 5301411431 1533682758",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="1344569458 1906306037",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1344569458",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API")
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = "AzernRobot"
    BOT_ID = "5909284642"
    BOT_NAME = "Azern Robot"
    owner_username = "SwapnoXD"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5909284642:AAHdPpIkEHHvbSUzDNvsvWxkWXEc7T4vWAY"
    API_ID = 12308732  # Your APP_ID from Telegram
    API_HASH = "a28b981438bfc9bb921563cf09bc4951"  # Your APP_HASH from Telegram
    OWNER_ID = 1626505310  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001969675336  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = [1626505310]
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://Lovely:LovelyMusic@lovely.zmqfspr.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "Lovely"  #
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    WORKERS = 8

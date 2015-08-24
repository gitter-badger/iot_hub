import sys
import ConfigParser
from paho.mqtt import publish

inifile=ConfigParser.SafeConfigParser()
inifile.read("./config.ini")

hostname=inifile.get("settings", "broker_name")
destinations="test"

class MessageSend:
    def messageSend(self, message=None):
        publish.single(destinations, message, hostname=hostname)

import requests

GAME = "value1"
NAME = "value2"
TURN = "value3"
UNKNOWN = "unknown"
DISCORD_MESSAGE_FORMAT = "{}, you're up! Turn number {} in game {}!"
PUSH_FORMAT = "You're up! Turn number {} in game {}!"
FOUR_FELLOWS = "Four fellows"

FOUR_FELLOWS_WEBHOOK = (
    "https://discordapp.com/api/webhooks/566111782725484544/" + 
    "8Ns1BHjvdEpndbTRXfZ5RR1UqH4SEgszEPhQEEbCiwjfALPT2S9h5APA5lx9PN4WpVDm"
)

class Player(object):
    def __init__(self, discord_name = None, discord_webhooks = None, push_notification = None):
        self.discord_name = discord_name or ""
        self.discord_webhooks = discord_webhooks or []
        self.push_notification = push_notification or ""
        
    
    def send(self, turn, game_name):
        s = DISCORD_MESSAGE_FORMAT.format(self.discord_name, turn, game_name)
        for webhook in self.discord_webhooks:
            if webhook == FOUR_FELLOWS_WEBHOOK and game_name != FOUR_FELLOWS:
                continue
            requests.post(webhook, json = {"content": s})
        s = PUSH_FORMAT.format(turn, game_name)
        if self.push_notification:
            requests.post(self.push_notification, data = s)
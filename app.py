from flask import Flask
from flask import request
import os
import flask
import requests
from player import Player

app = Flask(__name__)
FOUR_FELLOWS_WEBHOOK = (
    "https://discordapp.com/api/webhooks/566111782725484544/" + 
    "8Ns1BHjvdEpndbTRXfZ5RR1UqH4SEgszEPhQEEbCiwjfALPT2S9h5APA5lx9PN4WpVDm"
)
POND_WEBHOOK = (
    "https://discordapp.com/api/webhooks/568096818685018143/" + 
    "yFHEOELWfNhalc6_2hHIs6j9WOHwzWLWnjCJdpAxH7thH3Ej4PD8zHYL8Y_OeFbSFdex"
)

GAME = "value1"
NAME = "value2"
TURN = "value3"
UNKNOWN = "unknown"
message_format = "{}, you're up! Turn number {} in game {}!"
FOURFELLOWS = "Four fellows"
player_dictionary = {
    "tadpole":            Player(discord_name = "<@215701205710536706>", discord_webhooks = [FOUR_FELLOWS_WEBHOOK, POND_WEBHOOK]),
    "ezzy.nin":           Player(discord_name = "<@208034224522002445>", discord_webhooks = [FOUR_FELLOWS_WEBHOOK]),
    "AbyssMage":          Player(discord_name = "<@173982451687751680>", discord_webhooks = [FOUR_FELLOWS_WEBHOOK]),
    "The Wandering Mage": Player(discord_name = "<@215173275657961472>", discord_webhooks = [FOUR_FELLOWS_WEBHOOK, POND_WEBHOOK]),
    "m3marsh":            Player(push_notification = "https://notify.run/5YudarIyaCzwVx9j")
}
    
@app.route('/', methods = ['GET'])
def hi():
    return "<h1>Hi!!!</h1>"
    
@app.route('/process', methods=['GET', 'POST'])
def handle_webhook():
    data = request.get_json(force = True)
    game_name       = data.get(GAME, UNKNOWN)
    civ_player_name = data.get(NAME, UNKNOWN)
    turn            = data.get(TURN, UNKNOWN)
    if UNKNOWN in [game_name, civ_player_name, turn]:
        print "Invalid data"
        return "Fail"
    player = player_dictionary.get(civ_player_name)
    if player:
        player.send(turn, game_name)
    return "success"

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    print "app is running on port {}".format(port)
    app.run(host='0.0.0.0', port=port)
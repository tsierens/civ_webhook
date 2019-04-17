from flask import Flask
from flask import request
import os
import flask
import requests

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
    "tadpole": "<@215701205710536706>",
    "ezzy.nin": "<@208034224522002445>",
    "AbyssMage": "<@173982451687751680>",
    "The Wandering Mage": "<@215173275657961472>"
}

def send_to_discord(s, webhook):
    print "sending to discord"
    requests.post(webhook, json = {"content": s})
    
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
    player = player_dictionary.get(civ_player_name, civ_player_name)
    if game_name == FOURFELLOWS:
        send_to_discord(message_format.format(player, turn, game_name), FOUR_FELLOWS_WEBHOOK)
    send_to_discord(message_format.format(player, turn, game_name), POND_WEBHOOK)
    return "success"

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    print "app is running on port {}".format(port)
    app.run(host='0.0.0.0', port=port)
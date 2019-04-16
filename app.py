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
GAME = "value1"
NAME = "value2"
TURN = "value3"
UNKNOWN = "unknown"
message_format = "{}, you're up! Turn number {} in game {}!"
FOURFELLOWS = "Four fellows"
player_dictionary = {
    "tadpole": "@tadpole#3755",
    "ezzy.nin": "@EchoSEN#4393",
    "AbyssMage": "@Tay#0001",
    "The Wandering Mage": "@The Wandering Mage#9391"
}

def send_to_discord(s):
    requests.post(FOUR_FELLOWS_WEBHOOK, json = {"content": s})
    
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
        raise("Invalid data")
    player = player_dictionary.get(civ_player_name, civ_player_name)
    if game_name == FOURFELLOWS:
        send_to_discord(message_format.format(player, turn, game_name))
    else:
        print message_format.format(player, turn, game_name)
    return "success"

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    print "app is running on port {}".format(port)
    app.run(host='0.0.0.0', port=port)
from flask import Flask, jsonify, request
from game import Game
import threading
import time

app = Flask(__name__)

# Initialize the game
game = Game()

# To manage game updates in a separate thread
game_lock = threading.Lock()

@app.route('/start', methods=['POST'])
def start_game():
    global game
    with game_lock:
        game = Game()
    return jsonify({"status": "Game started"}), 200

@app.route('/jump', methods=['POST'])
def jump():
    with game_lock:
        game.jump()
    return jsonify({"status": "Dino jumped"}), 200

@app.route('/duck', methods=['POST'])
def duck():
    with game_lock:
        game.duck()
    return jsonify({"status": "Dino ducking"}), 200

@app.route('/unduck', methods=['POST'])
def unduck():
    with game_lock:
        game.unduck()
    return jsonify({"status": "Dino stopped ducking"}), 200

@app.route('/state', methods=['GET'])
def get_state():
    with game_lock:
        state = game.get_state()
    return jsonify(state), 200

def game_update():
    while True:
        time.sleep(1 / FPS)

# Run the game update in a separate thread
threading.Thread(target=game_update, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


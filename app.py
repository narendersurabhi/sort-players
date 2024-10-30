from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

players = ["Nikhil", "Ketan", "Karthik", "Hussain", "Ganesh", "Praveen", "Siva", "Gaurav", "Shravan", "Pandi", "Adarsh", "Trinadh", "Peter"]
comparisons = []

@app.route('/')
def index():
    if len(players) < 2:
        return render_template('finished.html', order=comparisons)
    player1, player2 = random.sample(players, 2)
    return render_template('compare.html', player1=player1, player2=player2)

@app.route('/compare', methods=['POST'])
def compare():
    winner = request.form['winner']
    loser = request.form['loser']
    comparisons.append((winner, loser))
    players.remove(winner)
    players.remove(loser)
    return jsonify({"status": "success"})

@app.route('/result')
def result():
    return jsonify({"order": comparisons})

if __name__ == '__main__':
    app.run(debug=True)

from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
app.config["SECRET_KEY"] = "I turn coffee into websites."

boggle_game = Boggle()
    
@app.route("/")
def show_board():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    return render_template('board.html', board=board, highscore=highscore)

@app.route("/search-word")
def search_word():
    word = request.args.get('word')
    board = session['board']
    result = boggle_game.check_valid_word(board, word)
    return jsonify({'result': result})

@app.route("/store-highscore", methods=['POST'])
def store_highscore():
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    if score > highscore:
        session['highscore'] = score
    #session['highscore'] = 0
    is_new_highscore = score > highscore
    return jsonify({'isnewhighscore': is_new_highscore})
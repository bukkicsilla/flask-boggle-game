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
    return render_template('board.html', board=board)

@app.route("/search-word")
def search_word():
    word = request.args.get('word')
    board = session['board']
    res = boggle_game.check_valid_word(board, word)
    return jsonify({'result': res})

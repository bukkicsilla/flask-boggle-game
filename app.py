from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
app.config["SECRET_KEY"] = "I turn coffee into websites."

boggle_game = Boggle()
    
@app.route("/")
def show_board():
    '''It created the board with random letters.'''
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    num_played = session.get("numplayed", 0)
    return render_template('board.html', board=board, highscore=highscore, num_played=num_played)

@app.route("/search-word", methods=['GET', 'POST'])
def search_word():
    '''It searches the given word on the board. It returns a message. '''
    word = request.args.get('word')
    board = session['board']
    result = boggle_game.check_valid_word(board, word)
    return jsonify({'result': result})

@app.route("/store-highscore", methods=['POST'])
def store_highscore():
    '''It saves the highscores and how many times the game was played.'''
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    num_played = session.get("numplayed", 0)
    session['numplayed'] = num_played + 1
    if score > highscore:
        session['highscore'] = score
    #session['highscore'] = 0
    #session['numplayed'] = 0
    is_new_highscore = score > highscore
    return jsonify({'isnewhighscore': is_new_highscore, 'numplayed': num_played+1})
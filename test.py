from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_show_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boogle Game</h1>', html)
            self.assertIn('board', session)
            self.assertIsNotNone(session.get('board'))
            self.assertIsNone(session.get('highscore'))

    
    def test_session_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [["S", "L", "U", "A", "M"], 
                                 ["C", "A", "T", "H", "Q"], 
                                 ["D", "O", "G", "K", "X"], 
                                 ["B", "U", "T", "E", "P"], 
                                 ["W", "I", "N", "N", "Y"]]
            res = client.get('/search-word?word=win')
            self.assertEqual(res.json['result'], 'ok')
    
    def test_store_highscore(self):
        with app.test_client() as client:
            res = client.post('/store-highscore', json = {"score": 3})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('"isnewhighscore": true', html)


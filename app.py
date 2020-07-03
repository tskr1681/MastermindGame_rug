from flask import Flask, request, render_template, url_for
from datetime import datetime
import math

from game import Game
from strategy_analyser import StrategyAnalyser


app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return f"""
    <h1>Hello heroku</h1>
    <p>It is currently {the_time}.</p>
    <img src="http://loremflickr.com/600/400" />
    <p><h1> <a href="{ url_for('game_') }"> Play Game </a></h1></p>
    """


@app.route('/game', methods=['GET', 'POST'])
def game_():
    game = Game()
    game.play()

    color_code={
        1: 'yellow',
        2: 'rgb(102, 0, 204)',
        3: 'red',
        4: 'rgb(0,102,0)',
        5: 'rgb(255, 204, 255)',
        6: 'rgb(0, 0, 255)',
    }

    code = (game.codemaker.code)
    moves = (game.moves)
    feedbacks = (game.feedback)
    log = game.log.split('\n')



    analyser = StrategyAnalyser(5)
    analyser.run_simulation()

    games = (analyser.number_of_games)
    codes = (analyser.codes)
    sc1 = (analyser.mathematician_codebreaker_score)
    sc2 = (analyser.logician_codebreaker_score)
    sc3 = (analyser.random_codebreaker_score)


    return render_template('game.html', color=color_code, code=code, moves=moves,\
                            feedbacks=feedbacks, winner=game.winner, log=log,\
                            games=games, codes=codes, sc1=sc1, sc2=sc2, sc3=sc3    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

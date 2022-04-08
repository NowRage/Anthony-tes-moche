# from crypt import methods
from flask import Flask, render_template, url_for, request, session, redirect
from label import str_TOO_YOUNGER
from module_tirage import premier_tirage, deuxieme_tirage
from module_gain import gain


app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route('/')
def homepage():
    return render_template('start.html')


@app.route('/', methods=['POST'])
def check_age():
    user_age = int(request.form['age'])
    if user_age < 18:
        session['error-form'] = str_TOO_YOUNGER
        return render_template('start.html')
    else:
        session['wallet'] = request.form['wallet']
        return redirect(url_for('board'))


@app.route('/board')
def board():
    return render_template('board.html')


@app.route('/board', methods=['POST'])
def check_mise():
    user_mise = int(request.form['mise'])
    if user_mise <= 0:
        print("La valeur doit être supérieure ou égale à 1.")

    else:
        session['mise'] = request.form['mise']
        tirage, new_deck = premier_tirage()
        session['premier_tirage'] = tirage
        session['deck'] = new_deck
        # print(tirage_)
        # return render_template('game.html')
        return redirect(url_for('game'))

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/gain')
def gain():
    return render_template('module_gain.py')
        
def choix_cartes(tirage):
    jeu = session[premier_tirage]
    for i in reversed:
        print(str(tirage.index(i)))
        choix = input('y/n:')
        if choix == 'y':
            jeu.append(i)
    return jeu

if __name__ == '__main__':
    app.run(debug=True)
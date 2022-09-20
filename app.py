from flask import Flask, render_template, request, redirect, url_for
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/', methods = ['get', 'post'])
def index():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        GameOfLife(int(height), int(weight))
        return redirect(url_for('live'))
    else:
        return render_template('index.html')

@app.route('/live/')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game = game)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
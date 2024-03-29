import random
import json
from   flask import Flask, render_template, request

'''Flask example v5: GET parameters.'''

# Flask initialization
# ----------------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)
# ----------------------------------------------------

# ----------------------------------------------------
@app.route('/')
def index():
    greeting: str = 'Hello World!'
    return greeting

# ----------------------------------------------------
@app.route('/hello/<name>')
def hello(name: str):
    greeting: str = f'Hello {name}!'
    return greeting

# ----------------------------------------------------
@app.route('/buy/<comic>/<volume>')
def buy(comic: str, volume: str):
    message: str = f'You have bought {comic}, volume {volume}.'
    return message


# Uses GET parameters
# ----------------------------------------------------
@app.route('/buy2')
def buy2():

    comic:  str = request.args.get('comic')
    volume: str = request.args.get('volume')

    message: str = f'You have bought {comic}, volume {volume}.'
    return message




# If return type is a string, Flask embeds it into
# a Response object automatically with a content type of 'html'.
# app.root_path has the path where app.py is located.
# ----------------------------------------------------
@app.route('/db')
def db():

    db: list[dict] = [
        {'anime':     'DawBio1 Adventures',
         'character': 'Pablo',
         'quote':     'Los exámenes son con Internet' },

        {'anime':     'DawBio1 Adventures',
         'character': 'Joan',
         'quote':     'Los exámenes son a mano' },

        {'anime':     'DawBio1 Adventures',
         'character': 'Amoròs',
         'quote':     'La última práctica es opcional' },

    ]

    choice: dict = random.choice(db)

    # html: str = render_template('index.html',
    #                             anime=choice['anime'],
    #                             character=choice['character'],
    #                             quote=choice['quote']
    #                             )

    html: str = render_template('index.html', **choice)

    return html



# If return type is a string, Flask embeds it into
# a Response object automatically with a content type of 'html'.
# app.root_path has the path where app.py is located.
# ----------------------------------------------------
@app.route('/db2/<id>')
def db2(id: int):

    db: list[dict] = [
        {'anime':     'DawBio1 Adventures',
         'character': 'Pablo',
         'quote':     'Los exámenes son con Internet' },

        {'anime':     'DawBio1 Adventures',
         'character': 'Joan',
         'quote':     'Los exámenes son a mano' },

        {'anime':     'DawBio1 Adventures',
         'character': 'Amoròs',
         'quote':     'La última práctica es opcional' },

    ]

    idnum = int(id)

    # html: str = render_template('index.html',
    #                             anime=choice['anime'],
    #                             character=choice['character'],
    #                             quote=choice['quote']
    #                             )
    choice: dict = db[idnum]
    response_json: str = json.dumps(choice, separators=(',', ':'), ensure_ascii=False)

    return response_json


# Main
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# ----------------------------------------------------

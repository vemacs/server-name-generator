import random
from flask import Flask

latin = []
with open('list.txt') as f:
    for l in f:
        line = l.strip().title()
        if line != '' and '\\' not in line and ',' not in line:
            latin.append(line)
suffix = ['MC', ' Cloud', ' Network', 'PVP', ' PVP', 'Craft', 'Block', 'Mine']

app = Flask(__name__)

@app.route('/')
def generate_name():
    return '<h1>' + random.choice(latin) + random.choice(suffix) + '</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

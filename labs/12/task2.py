'''
Authors: Cassandra Cabrera & Miek Menenedez
Date: March 11,2020
Purpose:
- analyzes the Pokemon API
- populates Pokemons names
'''

from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

endpoint = 'https://pokeapi.co/api/v2/pokemon'

@app.route('/')
def main():
    try:
        r = requests.get(endpoint)
        data = r.json()
    except:
        print('please try again')
    return render_template('home.html', data=data)
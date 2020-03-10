'''
Authors: Cassandra Cabrera & Mke Menedez
Date: March 11,2020
Purpose: 
	- uses the NASA API
	- populates the screen with a lunar happening 
	from the day Cass was born :)
'''
from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

my_key = 'E0OOjbmKmbNejDS9SduatRQnMqX8PMxr1QcevB9I'

payload = {
  'api_key': my_key,
  'start_date': '1999-10-25',
  'end_date': '1999-10-25'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

@app.route('/')
def main():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
    except:
        print('please try again')
    return render_template('nasa.html', data=data)
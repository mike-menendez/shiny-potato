'''
Authors: Cassandra Cabrera & Mike Menenendez
Date: March 9, 2020
Purpose:
	- satisfy Task 2 of Lab 11 for CST205
	- creates simple Hello World website using Flask
'''
from flask import Flask
# create an instance of the Flask class
app = Flask(__name__)
# route() decorator binds a function to a URL
@app.route('/hello')
def hello():
 return 'Hello world from Flask'
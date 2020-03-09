'''
Authors: Cassandra Cabrera & Mike Menenendez
Date: March 9, 2020
Purpose:
	- satisfy Task 3 of Lab 11 for CST205
	- creates list of favorite colors
'''
from flask import Flask, render_template 
from flask import Flask
from flask_bootstrap import Bootstrap

#defines my dictionary
stuff = {'seasons': ['fall','winter','summer','spring'],
		'favColors': ['forest green','dodger blue','sunshine yellow']
		}

# create an instance of the Flask class
#links to bootstrap template as well
app = Flask(__name__)
Bootstrap(app)

# route() decorator binds a function to a URL
@app.route('/hello')
def hello():
	return render_template('template.html', s_list=stuff)
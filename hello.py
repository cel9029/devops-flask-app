from flask import Flask


app = Flask(__name__)


@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p> <a href="/about">About Page</a>'
	
@app.route('/about')
def say_hello():
	return '<p>Hello, I am the about page!</p>'

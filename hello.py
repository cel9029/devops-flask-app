from flask import Flask


app = Flask(__name__)


@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p><a href="/about">About Page</a><a href="/contact">Contact Page</a>'
	
@app.route('/about')
def say_hello():
	return '<p>Hello, I am the about page!</p>'
    
@app.route('/contact')
def say_hello():
	return '<p>Email: c22455366@mytudublin.ie</p>'

from flask import Flask


app = Flask(__name__)


@app.route('/')
def say_hello():
	return '<p>Welcome, I am a Flask app!</p><a href="/about">About Page</a><a href="/contact">Contact Page</a>'
	
@app.route("/about")
def about():
    return '''
    <h1>About Page</h1>
    <p>This app uses Flask and Python.</p>
    <a href="https://flask.palletsprojects.com/">Flask Website</a><br>
    <a href="https://www.python.org/">Python Website</a>
    '''
    
@app.route('/contact')
def say_hello():
	return '<p>Email: C22455366@mytudublin.ie</p>'

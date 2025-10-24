from flask import Flask
import redis
import time
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
app = Flask(__name__)

@app.route('/')
def say_hello():
	data r.get('/')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']
	data = '<p>Welcome, I am a Flask app!</p><a href="/about">About Page</a><a href="/contact">Contact Page</a>'
	r.set('/', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data
	
@app.route("/about")
def about():
	data r.get('about')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']
	data = '<h1>About Page</h1><p>This app uses Flask and Python.</p><br><a href="https://flask.palletsprojects.com/">Flask Website</a><br><a href="https://www.python.org/">Python Website</a>'
    	r.set('/', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data
	
@app.route('/contact')
def contact():
	data r.get('contact')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']
	data = '<p>Email: C22455366@mytudublin.ie</p>'
	    r.set('/', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data

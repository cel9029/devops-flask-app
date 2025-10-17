#!/bin/bash

sudo apt -y update && sudo apt -y upgrade
sudo apt -y install nano vim python-is-python3
sudo apt -y install python3-venv python3-pip
python -m venv .my_venv
source .my_venv/bin/activate
pip install flask
cat << script < hello.py
from flask import Flask


app = Flask(__name__)


@app.route('/')
def say_hello():
	return '<p>Welcome, I am a Flask app!</p> <a href="/about">About Page</a><a href="/contact">Contact Page</a>'
	
@app.route('/about')
def say_hello():
	return '<p>Hello, I am the about page!</p>'

@app.route('/contact')
def say_hello():
	return '<p>Email: C22455366@mytudublin.ie</p>'
script


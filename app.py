from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
  return 'Index page'

@app.route('/hello')
def hello():
  return 'Hello world'

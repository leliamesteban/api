from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
  return 'Index page'

@app.route('/book', methods=['GET', 'POST'])
def book():
  if method == GET:
    return {"a": "b"} # JSON
  elif method == POST:
    pass
    # create new book if not already exists

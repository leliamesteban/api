from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

books = [
  {
    "title": "Smart plant factories",
    "subtitle": "",
    "authors": "", "", "",
  },
]

books = json.loads(books)

class Book(Resource):
  def get(self, name):
    if books['title'] == name:
      return books['title'], 200
     return "Book not found", 404
    
  def post(self, name):
    parser = reqparse.RequestParser()
    parser.add_argument("subtitle")
    parser.add_argument("author")
    args = parser.parse_args()
    
    if books['title'] == name:
      return "Book with title {} already exists".format(books['title']), 400
      
    book = {
      "title": title,
      "subtitle": args["subtitle"],
      "author": args["author"]
    }
    
    books.append(book)
    return book, 201
  
  def put(self, name):
  
  def delete(self, name):

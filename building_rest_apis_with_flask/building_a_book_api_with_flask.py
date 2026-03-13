from flask import Flask
import json

app = Flask(__name__)

with open('books.json') as file:
    books = json.load(file)

@app.route('/books/<book_id>')
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return book
    else:
        return f'No book with id {book_id}', 404

@app.route('/')
def index():
    return "Homepage"
app.run(debug=True)


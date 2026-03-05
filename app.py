from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from data_models import db, Author, Book

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        birthdate = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')
        
        new_author = Author(name=name, birth_date=birthdate, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()
        message = "Author successfully added!"
    return render_template('add_author.html', message=message)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    message = None
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')
        
        if author_id:
            new_book = Book(title=title, isbn=isbn, publication_year=publication_year, author_id=int(author_id))
            db.session.add(new_book)
            db.session.commit()
            message = "Book successfully added!"
    return render_template('add_book.html', authors=authors, message=message)

@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'title')
    search_query = request.args.get('search', '').strip()
    
    query = Book.query

    if search_query:
        search = f"%{search_query}%"
        query = query.filter(Book.title.like(search))

    if sort_by == 'author':
        books = query.join(Author).order_by(Author.name).all()
    else:
        books = query.order_by(Book.title).all()
        
    return render_template('home.html', books=books, sort_by=sort_by, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
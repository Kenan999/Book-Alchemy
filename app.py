"""Main Flask application for the Book Alchemy digital library."""
import os
from flask import Flask, render_template, request, redirect, url_for
from data_models import db, Author, Book

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
)

db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """Route to add a new Author to the database."""
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        birthdate = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')

        new_author = Author(
            name=name,
            birth_date=birthdate,
            date_of_death=date_of_death
        )
        db.session.add(new_author)
        db.session.commit()
        message = "Author successfully added!"
    return render_template('add_author.html', message=message)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """Route to add a new Book to the database."""
    message = None
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        rating = request.form.get('rating')
        author_id = request.form.get('author_id')

        if author_id:
            rating_val = int(rating) if rating else None
            new_book = Book(
                title=title,
                isbn=isbn,
                publication_year=publication_year,
                rating=rating_val,
                author_id=int(author_id)
            )
            db.session.add(new_book)
            db.session.commit()
            message = "Book successfully added!"
    return render_template('add_book.html', authors=authors, message=message)


@app.route('/')
def home():
    """Home route that displays books with search and sorting features."""
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

    success_message = request.args.get('success_message')

    return render_template(
        'home.html',
        books=books,
        sort_by=sort_by,
        search_query=search_query,
        success_message=success_message
    )


@app.route('/book/<int:book_id>')
def book_detail(book_id):
    """Route to display detail page for a specific Book."""
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)


@app.route(
    '/author/<int:author_id>'
)
def author_detail(author_id):
    """Route to display detail page for a specific Author."""
    author = Author.query.get_or_404(author_id)
    return render_template('author_detail.html', author=author)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """Route to delete a book and its author if it's the author's last book."""
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id
    title = book.title

    db.session.delete(book)
    db.session.commit()

    # Check if author has any other books left
    other_books_count = Book.query.filter_by(author_id=author_id).count()
    if other_books_count == 0:
        author = Author.query.get(author_id)
        if author:
            db.session.delete(author)
            db.session.commit()

    success_msg = (
        f'Deleted book "{title}" successfully!'
    )
    return redirect(url_for('home', success_message=success_msg))


@app.route('/author/<int:author_id>/delete', methods=['POST'])
def delete_author(author_id):
    """Route to delete an author and all their associated books."""
    author = Author.query.get_or_404(author_id)
    name = author.name

    db.session.delete(author)
    db.session.commit()

    success_msg = (
        f'Deleted author "{name}" and all their associated '
        'books successfully!'
    )
    return redirect(
        url_for('home', success_message=success_msg)
    )


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0', use_reloader=False)

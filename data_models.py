"""Data models for the digital library application."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """Author data model containing personal and biographical details."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(50))
    date_of_death = db.Column(db.String(50))

    def __repr__(self):
        return f'<Author {self.name}>'

    def __str__(self):
        return f"{self.name} (b. {self.birth_date})"


class Book(db.Model):
    """Book data model with connection to its Author."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(50))
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    author_id = db.Column(
        db.Integer, db.ForeignKey('author.id'), nullable=False
    )

    author = db.relationship(
        'Author',
        backref=db.backref('books', lazy=True, cascade='all, delete-orphan')
    )

    def __repr__(self):
        return f'<Book {self.title}>'

    def __str__(self):
        author_name = self.author.name if self.author else 'Unknown'
        return f"'{self.title}' by {author_name}"

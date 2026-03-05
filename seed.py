"""Script to seed the SQLite database with initial Authors and Books."""
from app import app, db
from data_models import Author, Book


def seed_db():
    """Drops any existing database tables, creates new ones, and seeds data."""
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        author1 = Author(name="J.K. Rowling", birth_date="1965-07-31", date_of_death="")
        author2 = Author(name="Douglas Adams", birth_date="1952-03-11", date_of_death="2001-05-11")
        author3 = Author(name="Jane Austen", birth_date="1775-12-16", date_of_death="1817-07-18")
        author4 = Author(name="George Orwell", birth_date="1903-06-25", date_of_death="1950-01-21")
        author5 = Author(name="Virginia Woolf", birth_date="1882-01-25", date_of_death="1941-03-28")

        db.session.add_all([author1, author2, author3, author4, author5])
        db.session.commit()

        b1 = Book(title="Harry Potter and the Sorcerer's Stone", isbn="9780590353427",
                  publication_year=1997, author_id=author1.id)
        b2 = Book(title="Harry Potter and the Chamber of Secrets", isbn="9780439064873",
                  publication_year=1998, author_id=author1.id)
        b3 = Book(title="The Hitchhiker's Guide to the Galaxy", isbn="9780345391803",
                  publication_year=1979, author_id=author2.id)
        b4 = Book(title="Pride and Prejudice", isbn="9780141439518",
                  publication_year=1813, author_id=author3.id)
        b5 = Book(title="Emma", isbn="9780141439587", publication_year=1815, author_id=author3.id)
        b6 = Book(title="1984", isbn="9780451524935", publication_year=1949, author_id=author4.id)
        b7 = Book(title="Animal Farm", isbn="9780451526342", publication_year=1945,
                  author_id=author4.id)
        b8 = Book(title="Mrs Dalloway", isbn="9780156628709", publication_year=1925,
                  author_id=author5.id)
        b9 = Book(title="To the Lighthouse", isbn="9780156907392", publication_year=1927,
                  author_id=author5.id)

        db.session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9])
        db.session.commit()

        print("Database seeded!")


if __name__ == '__main__':
    seed_db()

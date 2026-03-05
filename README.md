# Book Alchemy 📚

Welcome to **Book Alchemy**, a robust digital library application that lets you catalog, manage, and track your personal book collection. Built with Python, Flask, and SQLite, this application offers an elegant web interface to store details about your favorite authors and their books.

## ✨ Features

- **Author Management**: Easily add new authors to your database, listing their birth and death dates.
- **Book Inventory**: Keep track of the books you own. Add books with an ISBN, publication year, and a personal rating (out of 10).
- **Auto-Fetched Covers**: Utilizes the OpenLibrary API to automatically fetch and display book covers based on their ISBN.
- **Search and Sort**: Quickly find any book in your massive library using the keyword search, or sort your library by Book Title or Author Name.
- **Detail Views**: Dedicated profile pages for each Author (listing all their books) and each Book (showing full metadata).
- **Graceful Deletion**: Remove books from your collection. Cascade relationships ensure that deleting an author gracefully removes all of their associated books from your library as well.

## 🚀 Technologies Used

- **Backend**: Python 3, Flask
- **Database**: SQLite3, SQLAlchemy, Flask-SQLAlchemy (ORM)
- **Frontend**: HTML5, Vanilla CSS, Jinja2 Templating
- **External APIs**: OpenLibrary Covers API

## 🛠️ Installation & Setup

Follow these instructions to get a local copy of Book Alchemy up and running on your machine.

### Prerequisites

Ensure you have Python 3.8+ installed on your system. 

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Kenan999/Book-Alchemy.git
   cd Book-Alchemy
   ```

2. **Set Up a Virtual Environment** (Recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize and Seed the Database**
   You can populate the database with some example data right away:
   ```bash
   python3 seed.py
   ```
   *Note: This will create a local `data/library.sqlite` file if it doesn't already exist.*

5. **Run the Application**
   Start the local Flask development server:
   ```bash
   python3 app.py
   ```
   The application will be accessible at: `http://127.0.0.1:5000/`

## 📖 Usage Highlights

- **Adding an Author**: From the homepage, click "Add New Author". Fill out the form and submit.
- **Adding a Book**: Click "Add New Book". You must associate the book with a previously created author. Enter the ISBN to automatically get the book's cover image.
- **Rating a Book**: When adding a book, give it a rating from 1-10 to track your favorite reads!
- **Library Dashboard**: The homepage displays your collection. Use the dropdown to sort alphabetically, or use the search bar to find a specific title.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! If you'd like to improve Book Alchemy, please fork the repository and create a pull request.

## 📝 License

This project is licensed under the MIT License.

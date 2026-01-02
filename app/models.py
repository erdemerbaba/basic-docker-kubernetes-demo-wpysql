from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Book(db.Model):
    """Defines the Book model mappe to the books table in postgresql."""
    __tablename__ = 'books'
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.String(255),nullable=False)
    author = db.column(db.String(255), nullable=False)
    year = db.column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

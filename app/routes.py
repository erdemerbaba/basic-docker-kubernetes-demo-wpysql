from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Book

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """ Handles CREATE and READ operations. """
    if request.method == 'POST':
        # CREATE operation
        try:
            new_book = Book(
                title=request.form['title'],
                author=request.form['author'],
                year=int(request.form['year'])
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('main.index'))
        except ValueError:
            return "Error: Year must be a whole number.", 400
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while adding the book: {e}", 500

    # READ operation
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template('index.html', books=books)

@main_bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    """ Handles UPDATE operations. """
    book = db.get_or_404(Book, book_id)

    if request.method == 'POST':
        # UPDATE operation
        try:
            book.title = request.form['title']
            book.author = request.form['author']
            book.year = int(request.form['year'])
            db.session.commit()
            return redirect(url_for('main.index'))
        except ValueError:
            return "Error: Invalid year format.", 400
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while updating the book: {e}", 500

    # READ operation
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template('index.html', book_to_edit=book, books=books)

@main_bp.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    """ Handles DELETE operations. """
    book = db.get_or_404(Book, book_id)
    try:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('main.index'))
    except Exception as e:
        db.session.rollback()
        return f"An error occurred while deleting the book: {e}", 500

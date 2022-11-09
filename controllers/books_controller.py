from flask import Blueprint, render_template, request, redirect, url_for

from repositories import author_repository, book_repository
from models import Book, Author

# Define the `books` blueprint
books_blueprint = Blueprint('books', __name__)

# RESTful CRUD Routes
# INDEX     — GET '/books'
# NEW       — GET '/books/new'
# CREATE    — POST '/books'
# SHOW      — GET '/books/<id>'
# EDIT      — GET '/books/<id>/edit'
# UPDATE    — PUT '/books/<id>'
# DELETE    — DELETE '/books/<id>'

@books_blueprint.route('/books/')
def books():
    books_list = book_repository.select_all()
    return render_template('books/index.html.j2', title="All Books", books_list=books_list)

@books_blueprint.route('/books/new')
def new_book():
    authors_list = author_repository.select_all()
    return render_template('books/new.html.j2', title="New Book", authors_list=authors_list)

@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title       = request.form['title']
    page_count  = request.form['page_count']
    has_read    = 'has_read' in request.form
    author_id   = request.form['author_id']
    author      = author_repository.select(author_id) # XXX we don't really, really need the whole author
    book        = Book(title, page_count, has_read, author)
    book_repository.save(book)
    return redirect(url_for('.show_book', id=book.id))

@books_blueprint.route('/books/<int:id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html.j2', title=book.title, book=book)

@books_blueprint.route('/books/<int:id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect(url_for('.books'))

"""
# EDIT
# GET '/tasks/<id>/edit'
@books_blueprint.route('/books/<int:id>/edit')
def edit_task(id):
    task = book_repository.select(id)
    users_list = author_repository.select_all()
    return render_template('tasks/edit.html.j2', task=task, users_list=users_list)

# UPDATE
# PUT '/tasks/<id>'
@books_blueprint.route('/books/<int:id>', methods=['POST'])
def update_task(id):
    task = book_repository.select(id)
    task.description = request.form['description']
    user_id = request.form['user_id']
    if task.user.id != user_id:
        task.user = author_repository.select(user_id)
    task.duration    = request.form['duration']
    task.completed   = request.form['completed']
    # user_id     = request.form['user_id']
    # duration    = request.form['duration']
    # completed   = request.form['completed']
    # description = request.form['description']
    # user = user_repository.select(user_id)
    # task = Task(description, user, duration, completed, id=id)
    book_repository.update(task)
    return redirect('/tasks') # XXX should be /tasks/<id>.  XXX also use url_for!
"""
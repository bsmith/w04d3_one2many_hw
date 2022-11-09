from flask import Blueprint, render_template, request, redirect

from repositories import author_repository, book_repository
from models import Book, Author

# Define the `books` blueprint
books_blueprint = Blueprint('books', __name__)

# RESTful CRUD Routes

# INDEX
# GET '/books'
@books_blueprint.route('/books/')
def books():
    books_list = book_repository.select_all()
    return render_template('books/index.html.j2', books_list=books_list)

"""
# NEW
# GET '/tasks/new'
@books_blueprint.route('/books/new')
def new_task():
    users_list = author_repository.select_all()
    return render_template('tasks/new.html.j2', users_list=users_list)

# CREATE
# POST '/tasks'
@books_blueprint.route('/books', methods=['POST'])
def create_task():
    description = request.form['description']
    user_id     = request.form['user_id']
    duration    = request.form['duration']
    completed   = request.form['completed']
    user        = author_repository.select(user_id) # XXX we don't really, really need the whole user
    task        = Task(description, user, duration, completed)
    book_repository.save(task)
    return redirect('/tasks') # XXX should this not be /tasks/<id> XXX also use url_for!

# SHOW
# GET '/tasks/<id>'

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

# DELETE
# DELETE '/tasks/<id>'
@books_blueprint.route('/books/<int:id>/delete', methods=['POST'])
def delete_task(id):
    book_repository.delete(id)
    return redirect('/tasks') # XXX also use url_for!
"""
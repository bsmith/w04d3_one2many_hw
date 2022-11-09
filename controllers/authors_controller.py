from flask import Blueprint, render_template, request, redirect, url_for

from repositories import author_repository, book_repository
from models import Book, Author

# Define the `authors` blueprint
authors_blueprint = Blueprint('authors', __name__)

# RESTful CRUD Routes
# INDEX     — GET '/books'
# NEW       — GET '/books/new'
# CREATE    — POST '/books'
# SHOW      — GET '/books/<id>'
# EDIT      — GET '/books/<id>/edit'
# UPDATE    — PUT '/books/<id>'
# DELETE    — DELETE '/books/<id>'

@authors_blueprint.route('/authors/<int:id>')
def show_author(id):
    author = author_repository.select(id)
    return render_template('authors/show.html.j2', title=author.name, author=author)
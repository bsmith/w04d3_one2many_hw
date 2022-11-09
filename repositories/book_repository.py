from db.run_sql import run_sql

from models.book import Book
from models.author import Author
from repositories.author_repository import author_repository
from repositories.base import BaseRepository

class BookRepository(BaseRepository):
    SQL_SELECT_ALL = """SELECT * FROM books"""
    SQL_DELETE = """DELETE FROM books WHERE id = %s"""

    # This is a factory function that returns a factory function
    # A Factory Factory?!
    def get_mdo_factory(self):
        author_cache = {}
        def make_mdo_from_row(row):
            author_id = row['author_id']
            if author_id in author_cache:
                author = author_cache[author_id]
            else:
                author = author_repository.select(row['author_id'])
                author_cache[author_id] = author
            book = Book(
                row['title'],
                row['page_count'],
                row['has_read'],
                author,
                row['id'])
            return book
        return make_mdo_from_row

book_repository = BookRepository()

"""
def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = author_repository.select(result['user_id'])
        task = Task(result['description'], user, result['duration'], result['completed'], result['id'])
    return task

def delete_all():
    sql = "DELETE  FROM tasks"
    run_sql(sql)

def update(task):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)
"""

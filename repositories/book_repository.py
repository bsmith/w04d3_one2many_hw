from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

SQL_SELECT_ALL = """SELECT * FROM books"""

def make_mdo_from_row(row):
    author = None # author_repository.select(row['author_id'])
    book = Book(
        row['title'],
        row['page_count'],
        row['has_read'],
        author,
        row['id'])
    return book

def select_all():
    results = run_sql(SQL_SELECT_ALL)

    model_objects = [make_mdo_from_row(row) for row in results]
    return model_objects

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

def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(task):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)
"""

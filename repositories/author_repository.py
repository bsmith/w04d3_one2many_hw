from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from repositories.base import BaseRepository

class AuthorRepository(BaseRepository):
    SQL_SELECT_ALL = """SELECT * from authors"""
    SQL_SELECT = """SELECT * FROM authors WHERE id = %s"""

    def get_mdo_factory(self):
        def make_mdo_from_row(row):
            author = Author(
                row['name'],
                row['bio'],
                row['id'])
            return author
        return make_mdo_from_row

    def book_count(self, author):
        sql = """SELECT count(books.id) as book_count
            FROM books
            WHERE books.author_id = %s
            """
        values = [author.id]
        results = run_sql(sql, values)
        if results:
            return results[0]['book_count']
        return None

author_repository = AuthorRepository()

"""
def save(user):
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

def tasks(user):
    tasks = []

    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        task = Task(row['description'], row['user_id'], row['duration'], row['completed'], row['id'])
        tasks.append(task)
    return tasks
"""
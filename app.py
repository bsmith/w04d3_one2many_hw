from flask import Flask, render_template

# from controllers.books_controller import books_blueprint
# from controllers.authors_controller import authors_blueprint

def create_app():
    app = Flask(__name__)

    # https://stackoverflow.com/questions/46944596/is-autoescape-default-in-jinja2-flask
    app.jinja_options["autoescape"] = lambda _: True

    # app.register_blueprint(books_blueprint)
    # app.register_blueprint(authors_blueprint)

    @app.route('/')
    def home():
        return render_template('index.html.j2')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

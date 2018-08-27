# import render template function from  flask

from flask import render_template
# importation of app instance from app folder
from app import app


# views
@app.route('/')
# definition of view function
def index():
    """
    view root in page function that returns the index page and its data
    :return:
    """
    # render template function:
    # 1 takes in name of template file as the argument
    # 2 searches for template file in app/templates subdirectory and loads it
    message = 'Hello World'
    # message on the left represents variable on the template, message on the right represents variable in view function
    title = 'Home - Welcome to the best Movie review Website online'
    return render_template('index.html', title=title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html', id=movie_id)

# import render template function from  flask

from flask import render_template, request, redirect, url_for
# importation of app instance from app folder
from app import app

# import get movies, get movie and search movie functions from request module

from .request import get_movies, get_movie, search_movie


# views

@app.route('/')
# definition of view function
def index():
    """
    view root in page function that returns the index page and its data
    :return:

    """

    # Getting popular movie by creating variable popular movies where get_movies() function is called and popular passed as argument
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    # render template function:
    # 1 takes in name of template file as the argument
    # 2 searches for template file in app/templates subdirectory and loads it
    # message = 'Hello World'
    # message on the left represents variable on the template, message on the right represents variable in view function
    title = 'Home - Welcome to the best Movie review Website online'

    # get query from form submitted in index.html using request.args.get() with name of query passed in function and value returned
    search_movie = request.args.get('movie_query')

    if search_movie:
        # checking if value exists by using the redirect function redirecting to view function
        # pass url_for function that passes in search view function along with the dynamic movie_name assigning it to form input value
        return redirect(url_for('search', movie_name=search_movie))
    else:
        return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie,
                               now_showing=now_showing_movie)  # result from get_movies function passed to template


@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html', title=title, movie=movie)


# creating search view function displaying search items from api
@app.route('/search/<movie_name>')
# create search variable and pass dynamic variable movie_name
def search(movie_name):
    """
    view function to display search results
    :param movie_name:
    :return:
    """
    movie_name_list = movie_name.split
    # format movie_name to add + between multiple words
    movie_name_format = "+".join(movie_name_list)
    # call search movies and pass in formatted movie name
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    # pass search movies in template
    return render_template('search.html', movies=searched_movies)

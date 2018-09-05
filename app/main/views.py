# importation of app instance from app folder
# from app import app

# import get movies, get movie and search movie functions from request module

from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_movies, get_movie, search_movie
from .forms import ReviewForm, UpdateProfile
from ..models import Review, User
from flask_login import login_required
# import photos instance
from .. import db, photos


# views
# defining route decorators using the main blueprint instance
@main.route('/')
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
        return redirect(url_for('main.search', movie_name=search_movie))
    else:
        return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie,
                               now_showing=now_showing_movie)  # result from get_movies function passed to template


@main.route('/movie/<int:id>')
def movie(id):
    """
    view movie page function that returns the movie details page and its data
    :param id:
    :return:
    """
    movie = get_movie(id)
    title = f'{movie.title}'
    # call get reviews method taking in movie id
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html', title=title, movie=movie, reviews=reviews)


# creating search view function displaying search items from api
@main.route('/search/<movie_name>')
# create search variable and pass dynamic variable movie_name
def search(movie_name):
    """
    view function to display search results
    :param movie_name:
    :return:
    """
    movie_name_list = movie_name.split(" ")
    # format movie_name to add + between multiple words
    movie_name_format = "+".join(movie_name_list)
    # call search movies and pass in formatted movie name
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    # pass search movies in template
    return render_template('search.html', movies=searched_movies)


# new dynamic route for new_review function and pass in movie id
# add method to decorator telling flask to register function as handler for both GET and POST requests
# lack of methods argument enables the function to handle GET requests only
@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
# decorator login_required intercepting a request to check user authentication, redirecting user to login page if not
@login_required
def new_review(id):
    # creating instance of ReviewForm class and name it form
    form = ReviewForm()

    # call get_movie passing ID to get movie object with ID
    movie = get_movie(id)

    # data from form is verified by validators
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        # data from input fields is gathered and saved in new-review object
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        # response is redirected to movie_view function, movie ID passed in
        return redirect(url_for('main.movie', id=movie.id))

    title = f'{movie.title} review'
    # rendered when validate method returns false
    return render_template('new_review.html', title=title, review_form=form, movie=movie)


# route handled by profile view function
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        """
        querying database to find user according to username passed
        """
        abort(404) # abort stops request and returns response based on status code passed in, called when no user is found
        """
        abort called when no user is found
        else template is rendered when user is found
        """
    return render_template("profile/profile.html", user=user) # user passed in as variable in template


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    profile view function
    :param uname:
    instantiates UpdatedProfile form class
    :return:
    """
    user = User.query.filter_by(username = uname).first()
    """
    query database to find a user with same username
    """
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        """
        form validation
        """
        user.bio = form.bio.data
        """
        update content of user.bio property to fill in what user has submitted
        """

        db.session.add(user)
        db.session.commit()

        # user redirected to profile page where new bio can be seen
        return redirect(url_for('.profile', uname=user.username))
    # update html rendered if nothing is submitted
    return render_template('profile/update.html', form=form)


# route processing form submission request, route only accepts posts requests(method=POSTS)
@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user =User.query.filter_by(username = uname).first()
    """
    query database to pick a user with the same username passed in
    """
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        """
        flask request function used to check if any parameter with name photo has been passed into the request
        save method used to save file in our application
        """
        path = f'photos/{filename}'
        """
        path variable to file storage location created after saving
        """
        user.profile_pic_path = path
        """
        updating profile pic path property in user table and store path to file
        """
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))
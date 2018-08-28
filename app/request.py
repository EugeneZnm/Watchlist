from app import app
# import urllib request module enabling connection to API URL and send request
# import json modules that will format JSON response to a python dictionary
import urllib.request, json
from .models import movie

Movie = movie.Movie

# ACCESSING APP CONFIGURATION OBJECTS - CALL app.config['name of object']

# getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]


# function taking movie categories as an argument


def get_movies(category):
    """
    Function that gets the json response to our url request
    :param category:
    :return:
    """

    # .format method on base_url and pass in movie category and api_key
    # - replaces {} placeholders in base url with category and api key respectively
    get_movies_url = base_url.format(category, api_key)  # get_movies_url created as final url for API request

    # with context manager to send request using urllib.request.urlopen() function taking in get_movies_url as an
    # argument sending request as url
    with urllib.request.urlopen(get_movies_url) as url:
        # read function to read response which is stored in get_movies_data variable
        get_movies_data = url.read()

        # convert JSON response to python dictionary using js0n.loads function and pass in get_movies_data variable
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        # property results used to check if response contains any data
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            # process results function called taking in list of dictionary objects and return list of movie objects
            movie_results = process_results(movie_results_list)
    # list of movie objects
    return movie_results


# creating movie details page
def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)

    return movie_object


# function proces_results taking in list of dictionaries
def process_results(movie_list):
    """
    Function processing the movie result and transform them to a list of objects
    :param
    movie_list: aA list of dictionaries containing movie details
    :return:
    movie results: a list of movie objects
    """
    # list to store new movie objects
    movie_results = []

    # loop through the list of dictionaries using get() method and pass in keys so that vales can be accessed
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:  # if movie has a poster, movie object is created.
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            # values used to create movie object appended to empty list
            movie_results.append(movie_object)

    # list returned with movie objects
    return movie_results


# creating search request
def search_movie(movie_name):

    # new url for search request passing API Key and movie name
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    # creating request
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None
    # processing results
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results



import unittest

from models import movie

Movie = movie.Movie


class MovieTest(unittest.TestCase):
    """
    Test class to test the behaviour of the movie class
    """
    # setup method instantiating movie class to make self.new_movie object
    def setUp(self):
        """
        Set up method that will run before every test
        :return:
        """
        self.new_movie = Movie(1234, 'Python must be crazy', 'A thrilling new Python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    # test case checking if self.new_movie is instance of movie class
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ == '__main__':
    unittest.main()

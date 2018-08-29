# creating review class
class Review:
    all_reviews = []

    # init method taking in Movie id, Review title, image url and review itself
    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    # save review method appending review object to class variable all_reviews
    def save_review(self):
        Review.all_reviews.append(self)

    # clear review mthod clearing all items from list
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    # class get_reviews taking in IDs and
    @classmethod
    def get_reviews(cls, id):

        response = []

        # looping through all reviews in all_reviews list checking for reviews with similar id as movie id passed
        for review in cls.all_reviews:
            if review.movie_id == id:
                # appending reviews to repsonse list
                response.append(review)

        return response

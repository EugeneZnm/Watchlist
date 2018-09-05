from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# import flask class UserMixin that's passed into user model with methods to implement model configuration

from flask_login import UserMixin
from . import login_manager


# addition of class movie
class Movie:
    """
    Movie class to define Movie objects

    """

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count


# addition of class review
class Review:
    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(UserMixin, db.Model):
    """
    creation of User class enabling creation of new users
    pass in db,model as an argument connecting class to database allowing communication

    """
    # tablename variable allows giving the tables in our database proper names
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True) # email column added
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255)) # user biography column
    profile_pic_path = db.Column(db.String()) # stores path of profile photo
    password_hash = db.Column(db.String(255))
    """
    creation of columns using db.Column class, passing in the
    type of data stored as first argument 
    
    db.integer specifies that data in column should be an integer
    
    primary key set to true to set as primary key column, default value is false
    
    """
    username = db.Column(db.String(255))
    """
    db.string specifies data in column should be a string with a maximum of 255 characters
    
    """
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    """
    new column role id created and given integer type passing in db.ForeignKey class(tells SQLAlchemy that 
    it's a foreign key) and role.id(tells SQLAlchemy that id is of a role model as arguments'
    
    create connection between roles and users by using a foreign key
    foreignkey used to reference primary key in another table
    """

    def __repr__(self):
        """
        repr method makes debugging easier
        :return:
        """
        return f'User {self.username}'

    #decorator modifying load_user function by passing in user_id tofunction querying databse and gets a User with given id
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError(
            'You cannot read the password attribute')  # attribute error raised to block access to password property, preventing user access to property

    @password.setter
    def password(self, password):
        """
        generating password hash and passing hashed password as value to pass_secure column property
        to save to the databse

        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        Method verify password created to take in password, hash it and compare it to hashed password and check if they are the same
        :param password:

        """
        return check_password_hash(self.pass_secure, password)


class Role(db.Model):
    """
    ONE TO MANY RELATIONSHIP
    creating a role class that will define all different roles
    """
    __tablename__ = 'roles'

    # create two columns for the ID and name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")
    """
    - db.relationship used to create a virtual column that'll connect with the foreign key
    - pass in three arguments: class being referenced-user, backref - allowing access and setting of user class it's given
    the value of role so as to get role of user instance by running 'user.role'
    - lazy parameter - how SQLAlchemy will load projects
    - lazy option loaded on access and filtered before returning
    """

    def __repr__(self):
        return f'User{self.name}'

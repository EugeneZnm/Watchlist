import unittest
from app.models import User


class UserModelTest(unittest.TestCase):

    def setUp(self):
        """
        setUp method creating instance of User class
        pass in password property
        """
        self.new_user = User (password = 'banana')

    def test_password_setter(self):
        """
        test case ascertaining when password is hashed and pass_secure contains a value
        :return:
        """
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        """
        confirmation that application raises AttributeError when an attempt is made at accessing password property
        :return:
        """
        with self.assertRaises(AttributeError):
            self.new_user.password()

    def test_password_verification(self):
        """
        confirms password_hash can be verified when correct password is passed in
        :return:
        """
        self.assertTrue(self.new_user.verify_password('banana'))
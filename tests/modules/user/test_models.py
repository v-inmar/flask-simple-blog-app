import unittest
from datetime import datetime, timezone, timedelta
from app.modules.user.models.user_model import UserModel
from app.modules.user.models.user_pid_model import UserPIDModel
from app.modules.user.models.user_token_model import UserTokenModel
from config import TestConfig
from app import create_app, db

class UserModelCase(unittest.TestCase):

    def setUp(self):
        # Create an app context with test config
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all() # create database and tables
    
    def tearDown(self):
        db.session.remove() # Close session
        db.drop_all() # drop database and tables
        self.app_context.pop()
    
    def test_password_hashing(self):
        user = UserModel(firstname="john", lastname="doe", email="email@email.com")
        user.set_password("cat")
        self.assertFalse(user.check_password("dog")) # test for incorrect password
        self.assertTrue(user.check_password("cat")) # test for correct password


if __name__ == '__main__':
    unittest.main()
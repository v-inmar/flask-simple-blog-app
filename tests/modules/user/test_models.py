import unittest
import bcrypt
from sqlalchemy import inspect
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
    
    def test_user_creation(self):
        
        u1 = UserModel(firstname = "John", lastname = "Doe", email = "john.doe@email.com")
        u1.set_password("cat")
        db.session.add(u1)
        db.session.commit()

        retrieved_user1 = UserModel.query.filter_by(email="john.doe@email.com").first() or None
        self.assertIsNotNone(retrieved_user1)
        self.assertEqual(retrieved_user1.firstname, "John")
        self.assertEqual(retrieved_user1.lastname, "Doe")
        self.assertEqual(retrieved_user1.email, "john.doe@email.com")
        self.assertTrue(retrieved_user1.check_password("cat"))
        self.assertFalse(retrieved_user1.check_password("dog"))
    
    def test_password_hashing(self):
        user = UserModel(firstname="john", lastname="doe", email="email@email.com")
        user.set_password("cat")

        self.assertFalse(user.check_password("dog")) # test for incorrect password
        self.assertTrue(user.check_password("cat")) # test for correct password


if __name__ == '__main__':
    unittest.main()
# from unittest import TestCase
# from main import app
import sys
sys.path.append("website\__init__")
from website.__init__ import db
from website.models import User
from test.test_base import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin

# class TestAuth(TestCase):
    
#     def test_log_in(self):
#         with app.test_client() as client:
#             response = client.get('/log-in')
#             self.assertEqual(response.status_code, 200)

class TestSignUp(BaseTest):
    def test_get_sign_up(self):
        with self.app:
            
            
            
            response = self.app.get('/sign-up', follow_redirects=True)
            self.assertIn('/sign-up', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Sign Up', response.data)
            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))
            
    def test_sign_up_post_short_email(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='ok', firstName='bob', password1= '1234567', password2= '1234567'), follow_redirects=True)
            self.assertIn(b'Email must be greater than 3 characters', response.data)
            self.assertEqual(response.status_code, 200)
            user = db.session.query(User).filter_by(email='ok').first()
            self.assertFalse(user)
            self.assertIsNone(current_user.get_id())
            
    def test_sign_up_post_short_name(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='m', password1= '01234567', password2= '01234567'), follow_redirects=True)
            self.assertIn(b'First name must be greater than 1 character', response.data)
            self.assertEqual(response.status_code, 200)
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertFalse(user)
            self.assertIsNone(current_user.get_id())
            
    def test_sign_up_post_passwords_mismatched(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='kevin', password1= '01234567', password2= '1234567'), follow_redirects=True)
            self.assertIn(b'Passwords don&#39;t match', response.data)       
            self.assertEqual(response.status_code, 200)
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertFalse(user)
            self.assertIsNone(current_user.get_id())
            
# class TestLogin(BaseTest):
#     def test_get_login




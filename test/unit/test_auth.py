# from unittest import TestCase
# from main import app
import sys
sys.path.append("website\__init__")
from website.__init__ import db
from website.models import User
from test.test_base import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin



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
            
class TestLogin(BaseTest):
    def test_login_page_loads(self):
        with self.app:
            response = self.app.get('/log-in', follow_redirects=True)
            self.assertIn('/log-in', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Log in', response.data)
            
    def test_login_with_correct_data(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='mark', password1= '1234567', password2= '1234567'), follow_redirects=True)
            
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertTrue(user)
            
            response = self.app.post('/log-in', data=dict(email='test@gmail.com', password='1234567'), follow_redirects=True)
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertTrue(user)
            
            self.assertIn(b'Logged in successfully', response.data)
            self.assertEqual(response.status_code, 200)
            
class TestLogout(BaseTest):
    def test_logout_without_being_logged_in(self):
        with self.app:
            # self.app.post('/log-out', data=dict(email='test@gmail.com', password='1234567'), follow_redirects=True)
            response = self.app.get('/log-out', follow_redirects=False)
            self.assertEqual(response.status_code, 302)
            
    def test_logout_route_while_logged_in(self):
        with self.app:
            # sign up
            # log in
            response = self.app.get('/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    

            self.assertIn('/log-in', request.url)
            # after log out test current user is none
            self.assertFalse(current_user.is_active)


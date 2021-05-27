import sys
sys.path.append("website\__init__")
from website.__init__ import db
from website.models import Note, Team, User, Work
from test.test_base import BaseTest
from flask import request
from flask_login import current_user


class TestHome(BaseTest):
    def test_get_home_route(self):
        with self.app:
            response = self.app.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            
    def test_create_note(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='mark', password1= '1234567', password2= '1234567'), follow_redirects=True)
            
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertTrue(user)
            # assert user 1 is signed in
            self.assertEqual(current_user.get_id(), '1')
            # post a note
            response = self.app.post('/', data=dict(note='new note'), follow_redirects=True)
            # assert its in db
            note = db.session.query(Note).filter_by(data='new note').first()
            self.assertTrue(note)
            # assert that flash message called
            self.assertIn(b'Note added', response.data)
            
    def test_home_short_note(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='tests@gmail.com', firstName='mark', password1= '1234567', password2= '1234567'), follow_redirects=True)
            
            user = db.session.query(User).filter_by(email='tests@gmail.com').first()
            self.assertTrue(user)
            # assert user 1 is signed in
            self.assertEqual(current_user.get_id(), '1')
            # post a note
            response = self.app.post('/', data=dict(note='2'), follow_redirects=True)
            # assert its in db
            note = db.session.query(Note).filter_by(data='2').first()
            self.assertTrue(note)
            # assert that flash message called
            self.assertIn(b'Note added', response.data)
            
            
    def test_home_blank_note(self):
        with self.app:
            response = self.app.post('/sign-up', data=dict(email='test@gmail.com', firstName='mark', password1= '1234567', password2= '1234567'), follow_redirects=True)
            
            user = db.session.query(User).filter_by(email='test@gmail.com').first()
            self.assertTrue(user)
            # assert user 1 is signed in
            self.assertEqual(current_user.get_id(), '1')
            # post a note
            response = self.app.post('/', data=dict(note=''), follow_redirects=True)
            # assert its in db
            note = db.session.query(Note).filter_by(data='').first()
            self.assertFalse(note)
            # assert that flash message called
            self.assertIn(b'Note is too short', response.data)
            self.assertEqual(response.status_code, 200)       
    
            
            
            
            
            





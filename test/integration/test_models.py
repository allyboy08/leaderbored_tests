from website.models import Note, Work, User, Team
from test.test_base import BaseTest
import sys
sys.path.append("website\__init__")
from website.__init__ import db


class TestModels(BaseTest):
    def test_note_crud(self):
        with self.app_context():
            note = Note(data='test')
            
            result = db.session.query(Note).filter_by(data="test").first()
            self.assertIsNone(result)
            
            db.session.add(note)
            db.session.commit()
            
            result = db.session.query(Note).filter_by(data="test").first()
            self.assertIsNotNone(result)
            # assert note in db.session
            
            db.session.delete(note)
            db.session.commit()
            
            result = db.session.query(Note).filter_by(data="test").first()
            self.assertIsNone(result)
            
    def test_work(self):
        with self.app_context():
            work = Work(title='test', description='working', status='online', points=100)
            
            result = db.session.query(Work).filter_by(title='test').first()
            self.assertIsNone(result)
            
            db.session.add(work)
            db.session.commit()
            
            result = db.session.query(Work).filter_by(title="test").first()
            self.assertIsNotNone(result)
            
            db.session.delete(work)
            db.session.commit()
            
            result = db.session.query(Work).filter_by(title="test").first()
            self.assertIsNone(result)
    
    def test_user(self):
        with self.app_context():
            user = User(email='test@test.com', password='test', first_name='tester', team_leader=True, points=100)
            
            result = db.session.query(User).filter_by(email='test@test.com').first()
            self.assertIsNone(result)
            
            db.session.add(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(email='test@test.com').first()
            self.assertIsNotNone(result)
            
            db.session.delete(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(email="test@test.com").first()
            self.assertIsNone(result)
    
    def test_team(self):
        with self.app_context():
            team = Team(name='tester')
            
            result = db.session.query(Team).filter_by(name='tester').first()
            self.assertIsNone(result)
            
            db.session.add(team)
            db.session.commit()
            
            result = db.session.query(Team).filter_by(name='tester').first()
            self.assertIsNotNone(result)
            
            db.session.delete(team)
            db.session.commit()
            
            result = db.session.query(Team).filter_by(name="tester").first()
            self.assertIsNone(result)
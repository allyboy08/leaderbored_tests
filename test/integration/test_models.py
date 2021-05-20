from website.models import Note, Work, User, Team
from test.test_base import BaseTest
import sys
sys.path.append("website\__init__")
from website.__init__ import db


class TestModels(BaseTest):
    def test_crud(self):
        with self.app_context():
            note = Note(data='test')
            
            db.session.query(Note).filter_by(data="test").first()
            
            
            db.session.add(note)
            db.session.commit()
            
            assert note in db.session
            
            # db.session.delete(note)
            # db.session.commit()
            
    def test_work(self):
        with self.app_context():
            work = Work(title='test', description='working', status='online', points=100)
            
            db.session.query(Work).filter_by(title='test').first()
            
            db.session.add(work)
            db.session.commit()
            
            assert work in db.session
    
    def test_user(self):
        with self.app_context():
            user = User(email='test@test.com', password='test', first_name='tester', team_leader=True, points=100)
            
            db.session.query(User).filter_by(email='test@test.com').first()
            
            db.session.add(user)
            db.session.commit()
            
            assert user in db.session
    
    def test_team(self):
        with self.app_context():
            team = Team(name='tester')
            
            db.session.query(Team).filter_by(name='tester').first()
            
            db.session.add(team)
            db.session.commit()
            
            assert team in db.session
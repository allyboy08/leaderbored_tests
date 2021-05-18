from website.models import Note, Work, User, Team
from test.test_base import BaseTest
import sys
sys.path.append("website\__init__")
from website.__init__ import db


class TestModels(BaseTest):
    def test_crud(self):
        with self.app_context():
            note = Note(data='test1', date=17 / 5 / 2021, user_id=1)
            
            db.session.query(Note).filter_by(data="test").first()
            
            
            # db.session.add(note)
            # db.session.commit()
            
            # db.session.delete(note)
            # db.session.commit()
            
            
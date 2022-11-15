from flask import url_for, request
from flask_testing import TestCase
from application import app, db
from application.models import Users, Teams, Games, Picks

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db', SECRET_KEY = 'TEST_SECRET_KEY', DEBUG = True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):

        db.create_all()

        user1 = Users(username = 'TestName')
        db.session.add(user1)
        db.session.commit()

        team1 = Teams(team_name = 'TestTeam', team_city = 'TeamCity')
        team2 = Teams(team_name = 'TestTeam2', team_city = 'TestCity2')
        db.session.add(team1)
        db.session.add(team2)
        db.session.commit()

        game1 = Games(home_team = team1.id, away_team = team2.id, week_no = 1)
        db.session.add(game1)
        db.session.commit()

        pick1 = Picks(team_id = team1.id, user_id = user1.id, week_no = 1)
        db.session.add(pick1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_teams_get(self):
        response = self.client.get(url_for('week', username = 'TestName', week_no=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TestTeam', response.data)

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

class TestUser(TestBase):
    def test_user_get(self):
        response = self.client.get(url_for('user', username = 'TestName', id = 1 ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TestName', response.data)

class TestUpdate(TestBase):
    def test_update_get(self):
        response = self.client.get(url_for('update', week_no = 1, user_id = 1, team = 'TestTeam' ), follow_redirects = True)
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id = 1 ))
        assert request.path == url_for('home')

class TestAddUser(TestBase):
    def test_add_user(self):
        response = self.client.post(url_for('home'), data = dict(username = 'TestName'), follow_redirects=True )
        self.assertIn(b'TestName', response.data)


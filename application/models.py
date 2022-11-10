from application import db

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    team_city = db.Column(db.String(30), nullable=False)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    lives = db.Column(db.Integer(), nullable=False, default = 3)

class Games(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.Integer)
    away_team = db.Column(db.Integer)
    week_no = db.Column(db.Integer)
    home_score = db.Column(db.Integer, default = 0)
    away_score = db.Column(db.Integer, default = 0)
    win_team = db.Column(db.Integer, default = 1)

class Picks(db.Model):
    pick_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    uteam_id = db.Column(db.Integer)



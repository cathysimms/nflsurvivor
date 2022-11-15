from application import db

class Teams(db.Model):
    __tablename__='teams'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    team_city = db.Column(db.String(30), nullable=False)
    picks = db.relationship('Picks', backref='teamspbr')
   

class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    # first_name = db.Column(db.String(30), nullable=False)
    # surname = db.Column(db.String(30), nullable=False)
    # email = db.Column(db.String(30), nullable=False, unique=True)
    # lives = db.Column(db.Integer(), nullable=False, default = 3)
    picks = db.relationship('Picks', backref='usersbr')


class Games(db.Model):
    __tablename__='games'
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column('home_team', db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team = db.Column('away_team', db.Integer, db.ForeignKey('teams.id'), nullable=False)
    week_no = db.Column(db.Integer, nullable=False)
    # home_score = db.Column(db.Integer, default = 0)
    # away_score = db.Column(db.Integer, default = 0)
    # complete = db.Column(db.Boolean, default=False)
    # home_win = db.Column(db.Boolean, default=False)
    # away_win = db.Column(db.Boolean, default=False)
    #picks = db.relationship('Picks', backref='gamesbr')
    home = db.relationship('Teams', foreign_keys=[home_team])
    away = db.relationship('Teams', foreign_keys=[away_team])

class Picks(db.Model):
    __tablename__='picks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id',db.Integer, db.ForeignKey('users.id'), nullable=False)
    #game_id = db.Column('games_id',db.Integer, db.ForeignKey('games.id'), nullable=False)
    team_id = db.Column('team_id',db.Integer, db.ForeignKey('teams.id'),  nullable=False)
    week_no = db.Column('week_no', db.Integer)



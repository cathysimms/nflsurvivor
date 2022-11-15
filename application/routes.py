from application import app, db
from application.forms import HomeForm
from application.models import Games, Teams, Picks, Users
from flask import render_template, request, redirect, url_for

@app.route("/", methods=['GET','POST'])
def home():
    form = HomeForm()
    all_users = Users.query.all()
    all_picks = db.session.query(Picks, Teams).join(Teams).all()

    if request.method =='POST':
        if form.validate_on_submit():
            username = form.username.data
            users = Users.query.filter_by(username = username).all()
            
            for user in users:
                if username == user.username:
                    return redirect(url_for('user', username = user.username, id = user.id))  
            
            new_user = Users(username = username)
            db.session.add(new_user)
            db.session.commit()
            
            for i in range(1,19):
                new_pick = Picks(user_id = new_user.id, week_no = i, team_id = 33)
                db.session.add(new_pick)
            db.session.commit()
            
            return redirect(url_for('user', username = new_user.username, id = new_user.id))

    else:
        return render_template('home.html', form = form, all_users = all_users, all_picks = all_picks)

@app.route("/<username>/<int:id>", methods =['GET','POST'])
def user(username, id):
    #form = UserForm() 
    all_picks = db.session.query(Picks, Teams).join(Teams).all()
    user = Users.query.filter_by(id = id).first()

    return render_template('user.html', all_picks = all_picks, user = user) 
    
@ app.route("/<username>-week<int:week_no>", methods=['GET', 'POST'])
def week(username, week_no):
    
    user = Users.query.filter_by(username = username).first()
    all_picks = db.session.query(Picks, Teams).join(Teams).all()
    all_user_picks = db.session.query(Picks, Teams).join(Teams).filter(Picks.user_id == user.id).all()
    user_picks=[]
    for pick, team in all_user_picks:
        user_picks.append(team.team_name)

    home_teams = []
    away_teams = []

    all_games = Games.query.filter_by(week_no = week_no).all()
    num = Games.query.filter_by(week_no = week_no).count()

    for game in all_games:
        home_num = Teams.query.filter_by(id = game.home_team).first()
        away_num = Teams.query.filter_by(id = game.away_team).first()
        
        home_teams.append(home_num.team_name)
        away_teams.append(away_num.team_name)
        

    return render_template('week.html', num = num ,home_teams = home_teams, away_teams = away_teams, week_no = week_no, user = user, all_picks = all_picks, user_picks = user_picks)

@app.route('/update/<int:week_no>/<int:user_id>/<team>', methods=['GET','POST'])
def update(week_no, user_id, team):
    
    prev_pick = Picks.query.filter_by(user_id = user_id).all()
    user= Users.query.filter_by(id = user_id).first()
    username = user.username
    teamid = Teams.query.filter_by(team_name = team).first()

    for p in prev_pick:
        
        if p.team_id == teamid.id:
           
            return redirect(url_for('week', username = username, week_no = week_no))
   
    uppic = Picks.query.filter_by(week_no = week_no, user_id = user_id).first()
    uppic.team_id = teamid.id
    db.session.commit()

    return redirect(url_for('week', username = username, week_no = week_no))

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):

    user = Users.query.filter_by(id = id).first()
    picks = Picks.query.filter_by(user_id = id).all()

    db.session.delete(user)
    for pick in picks:
        db.session.delete(pick)
    
    db.session.commit()

    return redirect(url_for('home'))

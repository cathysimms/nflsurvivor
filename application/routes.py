from application import app
from application.forms import HomeForm, UserForm
from application.models import Games, Teams
from flask import render_template, request, redirect, url_for

@app.route("/", methods=['GET','POST'])
def home():
    form = HomeForm()

    if request.method =='POST':
        username = form.username.data
        return redirect(url_for('user', username = username))
    else:
        return render_template('home.html', form = form)

@app.route("/<username>", methods =['GET','POST'])
def user(username):
    form = UserForm()
    week_no = "choose"
    home_teams = []
    away_teams = []
    if request.method =='POST':
        week_no = form.week.data
        all_games = Games.query.filter_by(week_no = week_no).all()
        for game in all_games:
            home_num = Teams.query.filter_by(id = game.home_team).first()
            away_num = Teams.query.filter_by(id = game.away_team).first()
            home_teams.append(home_num.team_name)
            away_teams.append(away_num.team_name)
        return render_template('user.html', name = username, form=form, week_no = week_no, home_teams = home_teams, away_teams = away_teams)
    else:
        return render_template('user.html', name = username, form=form, week_no = week_no)
    
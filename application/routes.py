from application import app
from application.forms import HomeForm, UserForm
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
    return render_template('user.html', name = username, form=form)
    
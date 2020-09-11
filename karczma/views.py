# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, flash
from karczma import app
from datetime import datetime
from karczma.forms import SessionForm, LoginForm, RegisterForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import os
from karczma.models import Session, User
# Views


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form=LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Niepoprawny login lub hasło')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)

        return redirect(url_for('index'))

    return render_template('login.html', form=form)

#Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/rejestruj', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form= RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Rejestracja zakończona pomyślnie')
        redirect(url_for('login'))

    return render_template('register.html', form=form)
    


#User profile

#Session creator
@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add_session():
    form = SessionForm()

    if form.validate_on_submit():
        title = form.title.data
        game = form.game.data
        description = form.description.data
        max_players = form.max_players.data
        dates = form.dates.data
        sesja = Session(title=title, system=game, description=description, dates=dates, max_players = max_players)
        db.session.add(sesja)
        db.session.commit()
        flash(f'Zapisano sesję {title}')
        return redirect(url_for('index'))

    return render_template('add.html', form=form)

#Session view

#Sessions list

#404



if __name__ == "__main__":
    app.run(DEBUG=True)
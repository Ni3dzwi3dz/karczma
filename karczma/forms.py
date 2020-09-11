# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, ValidationError, Email, EqualTo
from karczma.models import User

class SessionForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    game = StringField('System', validators=[DataRequired()])
    description = StringField('Opis', validators=[DataRequired()])
    max_players = StringField('Ilość graczy')
    dates = StringField('Dostępne daty', validators=[DataRequired()])

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        
        return True

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj mnie')


class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    email = StringField('Adres email', validators=[DataRequired(), Email()])
    password = PasswordField ('Hasło', validators=[DataRequired()])
    password2 = PasswordField ('Powtórz hasło', validators=[DataRequired(),EqualTo('password')])

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError('Nazwa użytkownika jest już zajęta')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError('Do tego adresu e-mail przypisano już użytkownika')


    
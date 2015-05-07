# -*- coding: utf8 -*-

from wtforms import (Form, StringField, TextAreaField, DateTimeField,
                     PasswordField, BooleanField, validators)


class PostForm(Form):
    title = StringField('title', [validators.Length(min=1, max=255)])
    text = TextAreaField('article', [validators.Length(min=1)])
    browse_time = DateTimeField('time')


class LoginForm(Form):
    username = StringField('username', [validators.length(min=1, max=255)])
    password = PasswordField('password', [validators.length(min=1, max=255)])
    rememberme = BooleanField('rememberme')

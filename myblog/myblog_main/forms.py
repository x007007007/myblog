# -*- coding: utf8 -*-
from ajaxWtforms import AjaxForm
from wtforms import (Form, StringField, TextAreaField, DateTimeField,
                     PasswordField, BooleanField, validators)



class PostForm(AjaxForm):
    title = StringField('title', [validators.Length(min=1, max=255)])
    text = TextAreaField('article', [validators.Length(min=1)])
    browse_time = DateTimeField('time')


class LoginForm(AjaxForm):
    username = StringField('username', [validators.length(min=1, max=255)])
    password = PasswordField('password', [validators.length(min=1, max=255)])
    rememberme = BooleanField('rememberme')


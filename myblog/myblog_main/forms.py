# -*- coding: utf8 -*-
from ajaxWtforms import AjaxForm, ValidatorSchema
from wtforms import (Form, StringField, TextAreaField, DateTimeField,
                     PasswordField, BooleanField, validators)



class PostForm(AjaxForm):
    title = StringField('title', [validators.Length(min=1, max=255)])
    text = TextAreaField('article', [validators.Length(min=1)])
    browse_time = DateTimeField('time')


class TestForm(AjaxForm):
    a = StringField('title')
    b = StringField('test')
    c = StringField('tttt')
    def cb(self, data, key):
        pass
    v1 = ValidatorSchema((a, b, c), [cb])




class LoginForm(AjaxForm):
    username = StringField('username', [validators.length(min=1, max=255)])
    password = PasswordField('password', [validators.length(min=1, max=255)])
    rememberme = BooleanField('rememberme')


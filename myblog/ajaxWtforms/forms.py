# -*- coding: utf8 -*-
from jinja2 import Environment, PackageLoader
from wtforms import (Form, StringField, TextAreaField, DateTimeField,
                     PasswordField, BooleanField, validators)
from wtforms.form import BaseForm, FormMeta, with_metaclass
from .views import ajax_wtforms_bp, View
__author__ = 'xxc'
from .views import ajax_wtforms_bp
env = Environment(loader=PackageLoader('ajaxWtforms', 'templates'))




class AjaxFormMeta(FormMeta):
    def __init__(cls, name, bases, attrs):
        cls._unbound_validators = None
        if cls.__module__ not in [b'wtforms.compat', b'ajaxWtforms.forms']:
            view = View(cls)
            ajax_wtforms_bp.route(view.get_path(), methods=['GET', 'POST'])(view)
            print view.get_path(), view.__name__
        super(AjaxFormMeta, cls).__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if cls._unbound_validators == None:
            cls._unbound_validators = []
            for name in dir(cls):
                if not name.startswith('_'):
                    unbound_validators = getattr(cls, name)
                    if hasattr(unbound_validators, '_from_validator'):
                        cls._unbound_validators.append((name, unbound_validators))
        return super(AjaxFormMeta, cls).__call__(*args, **kwargs)


class AjaxForm(with_metaclass(AjaxFormMeta, Form)):
    def __render__(self):
        template = env.get_template('form.tpl')
        return template.render(form=self)

    def __unicode__(self):
        return self.__render__()

    def __str__(self):
        return self.__render__().encode('utf-8')


if __name__ == "__main__":
    form = AjaxForm(data={"text":"1.2.1..2"})
    print(form.validate(), form.errors)
from __future__ import unicode_literals
from flask import Blueprint, request, url_for
from flask import render_template
import pprint

ajax_wtforms_bp = Blueprint('ajax_wtforms', __name__, template_folder="templates", static_folder='static', static_url_path='/static/ajaxforms')


class View(object):
    def __init__(self, Form):
        self.Form = Form
        self.form = Form()
        self.__name__ = Form.__name__

    def __call__(self):
        from .forms import AjaxForm
        Form, form = self.Form, self.form
        assert issubclass(Form, AjaxForm)
        assert isinstance(form, Form)
        if request.method == 'GET':
            return self.GET()
        elif request.method == 'POST':
            return self.POST()
        return pprint.pformat(form._fields)

    def GET(self):
        from .forms import AjaxForm
        Form, form = self.Form, self.form
        assert issubclass(Form, AjaxForm)
        assert isinstance(form, Form)
        for key in form._fields:
            pprint.pprint(dir(form._fields))
        return render_template("test.tpl" , fields=form._fields)


    def POST(self):
        for key in request.args:
            print request.args[key]
        print()
        return ""

    def get_path(self):
        return ("/{}/{}".format(self.Form.__module__.replace(".", "/"), self.__name__))

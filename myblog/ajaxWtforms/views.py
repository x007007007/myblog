from __future__ import unicode_literals
from flask import Blueprint
import pprint

ajax_wtforms_bp = Blueprint('ajax_wtforms', __name__, template_folder="templates")


class View(object):
    def __init__(self, Form):
        self.Form = Form
        self.__name__ = Form.__name__

    def __call__(self, *args, **kwagrs):
        from .forms import AjaxForm
        Form = self.Form
        assert issubclass(Form, AjaxForm)
        form=Form()
        return pprint.pformat(form._fields)


    def get_path(self):
        return ("/{}/{}".format(self.Form.__module__.replace(".", "/"), self.__name__))

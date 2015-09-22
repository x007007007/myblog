from __future__ import unicode_literals
from flask import Blueprint, request, url_for
import pprint

ajax_wtforms_bp = Blueprint('ajax_wtforms', __name__, template_folder="templates")


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
        fields_html = []
        for key in form._fields:
            fields_html.append(unicode(form._fields[key]))
        return """
        <html>
        <body>
            <form method="POST">
                <ul>
                <li>{}</li>
                </ul>
                <button> send </button>
            </form>
        </body>
        </html>
        """.format("\n</li><li>".join(fields_html))

    def POST(self):
        return "wait"

    def get_path(self):
        return ("/{}/{}".format(self.Form.__module__.replace(".", "/"), self.__name__))

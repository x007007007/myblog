# -*- coding:utf8 -*-

from flask import Blueprint
pages = Blueprint('myblog_main', __name__, template_folder="templates")
del Blueprint
# -*- coding:utf8 -*-
from lib import Blueprint
pages = Blueprint('myblog_main', __name__, template_folder="templates")
del Blueprint

from flask_login import LoginManager
login_manager = LoginManager()
del LoginManager
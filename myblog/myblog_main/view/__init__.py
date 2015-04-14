# -*- coding:utf8 -*-
from flask import render_template
from ..models import Commit, Keyword, Article, db
from .. import pages


@pages.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.tpl', articals=articles)
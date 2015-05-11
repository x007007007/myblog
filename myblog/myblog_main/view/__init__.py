# -*- coding:utf8 -*-
import authorization
from flask import render_template, request, redirect, url_for, flash, Response, session
from ..models import Commit, Keyword, Article, db
from ..forms import PostForm
from .. import pages
from ..lib import View
from ..models import WebSession, User
from .. import login_manager
from flask_login import login_required
from flask_login import logout_user



@pages.route('/')
class Index(View):
    @staticmethod
    def getorpost():
        articles = Article.query.all()
        return render_template('index.tpl', articals=articles)


@pages.route('/post')
class Post(View):
    @staticmethod
    @login_required
    def post():
        form = PostForm(request.form)
        if form.validate():
            article = Article(form.title.data, form.text.data)
            s = db.session()
            s.add(article)
            s.commit()
            flash('success')
            return redirect(url_for('.Index'))
        return render_template('post.tpl', form=form)

    @staticmethod
    @login_required
    def get():
        form = PostForm()
        return render_template('post.tpl', form=form)


@pages.route('/commit/<int:test>')
class Commit(View):
    @staticmethod
    def get(test=1):
        return ('sss%d' % test)







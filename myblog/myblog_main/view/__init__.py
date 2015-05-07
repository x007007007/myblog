# -*- coding:utf8 -*-
from flask import render_template, request, redirect, url_for, flash, Response, session
from ..models import Commit, Keyword, Article, db
from ..forms import PostForm, LoginForm
from .. import pages
from ..lib import View
import sys


@pages.route('/')
class Index(View):
    @staticmethod
    def getorpost():
        articles = Article.query.all()
        return render_template('index.tpl', articals=articles)


@pages.route('/post')
class Post(View):
    @staticmethod
    def post():
        form = PostForm(request.form)
        if form.validate():
            article = Article(form.title.data, form.text.data)
            s = db.session()
            s.add(article)
            s.commit()
            flash('success')
            return redirect(url_for('.index'))
        return render_template('post.tpl', form=form)

    @staticmethod
    def get():
        form = PostForm()
        return render_template('post.tpl', form=form)

@pages.route('/commit/<int:test>')
class Commit(View):
    @staticmethod
    def get(test=1):
        return 'sss', 'sss'



@pages.route('/login', methods=['GET', 'POST'])
class Login(View):
    @staticmethod
    def post():
        form = LoginForm(request.form)
        flash("Logged in successfully: %s" % (form.username.data,))
        return redirect(url_for("myblog_main.Index"))

    @staticmethod
    def get():
        form = LoginForm()
        return render_template("login.tpl", form=form)

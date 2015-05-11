# -*- coding: utf8 -*-
from flask import render_template, request, redirect, url_for, flash, Response, session
from ..models import db
from ..forms import LoginForm
from .. import pages
from ..lib import View
from ..models import WebSession, User
from .. import login_manager
from flask_login import login_required
from flask_login import logout_user
from flask_login import login_user


@login_manager.user_loader
def load_user(user_uuid):
    """
    通过用户id登陆用户
    """
    return User.query.filter_by(uuid=user_uuid).first()

@login_manager.request_loader
def load_user_from_request(request):
    """
    通过session来直接登陆
    """
    return None

login_manager.login_view = ".Login"

@pages.route('/login')
class Login(View):
    @staticmethod
    def post():
        form = LoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.is_vaild_pasword(form.password.data):
                login_user(user)
                flash("Logged in successfully: %s" % (form.username.data,))
                # 存在xss风险
                return redirect(request.args.get('next', url_for(".Index")))
            else:
                form.password.errors.append("error password")
        return render_template("login.tpl", form=form)

    @staticmethod
    def get():
        form = LoginForm()
        return render_template("login.tpl", form=form)


@login_required
@pages.route('/logout')
class Logout(View):
    @staticmethod
    def get():
        logout_user()


@pages.route('/register')
class Register(View):
    @staticmethod
    def get():
        form = LoginForm()
        return render_template('login.tpl', form=form)

    @staticmethod
    def post():
        form = LoginForm(request.form)
        if form.validate():
            dbq_session = db.session()
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            dbq_session.add(user)
            dbq_session.commit()
            return redirect(url_for('.Login'))
        return render_template('login.tpl', form=form)
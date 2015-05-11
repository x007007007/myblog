# -*- coding:utf8 -*-
from . import MyBlogBaseModel, db, MyBlogBaseModelClassMaxin
from sqlalchemy import Column, String, DateTime, Integer, Binary
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import datetime
import time
import hashlib
import warnings

class User(MyBlogBaseModel):
    __tablename__ = 'user'
    uuid = Column(String(64), primary_key=True)
    username = Column(String(64), unique=True)
    security = Column(Binary(64))
    sessions = relationship("WebSession", backref="websession")

    @classmethod
    def create_user(cls, name, pswd):
        session = db.session()
        user = cls()
        user.name = name
        user.set_password(pswd)
        session.add(user)
        session.commit()

    def is_vaild_pasword(self, pswd):
        return self.security == hashlib.sha512(self.username + pswd).digest()

    def set_password(self, pswd):
        self.security = hashlib.sha512(self.username + pswd).digest()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uuid


class WebSession(db.Model, MyBlogBaseModelClassMaxin):
    __tablename__ = 'websession'

    session = Column(String(64), primary_key=True)
    lifetime = Column(Integer)
    user_uuid = Column(String(64), ForeignKey('user.uuid'))
    login_time = Column(DateTime)
    last_query_time = Column(DateTime)
    info = Column(String)

    def __init__(self, *args, **kwargs):
        self.session = self.get_new_uuid()
        self.login_time = self.get_current_datetime()
        if kwargs.pop('session'): warnings.warn("should't set this value")
        if kwargs.pop('login_time'): warnings.warn("should't set this value")
        super(WebSession, self).__init__(*args, **kwargs)

    @classmethod
    def create_session(cls, user):
        assert isinstance(user, User)
        ws = cls()
        ws.user_uuid = user.uuid


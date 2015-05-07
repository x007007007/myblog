from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, DateTime, Integer, Binary
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from flask import current_app
from uuid import uuid1
import datetime
import time


db = SQLAlchemy()


class MyBlogBaseModel(db.Model):
    __abstract__ = True

    uuid = Column(String(64), primary_key=True)
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    @classmethod
    def get_new_uuid(cls):
        return "%s_%s" % (cls.__name__, uuid1().hex)

    @classmethod
    def get_current_datetime(cls):
        return datetime.datetime.fromtimestamp(time.time())

    def __init__(self, uuid=None, create_time=None, *args, **kwargs):
        self.uuid = uuid if uuid else self.get_new_uuid()
        self.create_time = create_time if create_time else self.get_current_datetime()
        super(MyBlogBaseModel, self).__init__(*args, **kwargs)


class Commit(MyBlogBaseModel):
    __tablename__ = u'commit'

    article_uuid = Column(String(64), ForeignKey('article.uuid'))
    text = Column(String)


class Keyword(MyBlogBaseModel):
    __tablename__ = u'keyword'

    word = Column(String(32), primary_key=True)


class Article(MyBlogBaseModel):
    __tablename__ = u'article'

    title = Column(String(255))
    text = Column(String)
    commits = relationship("Commit", backref="commit")

    def __init__(self, title=None, text=None, *args, **kwargs):
        self.title = title
        self.text = text
        self.create_time = datetime.datetime.fromtimestamp(time.time())
        super(Article, self).__init__(*args,**kwargs)


class User(db.Model):
    __tablename__ = 'user'
    uuid = Column(String(64), primary_key=True)
    username = Column(String(64))
    security = Column(String(64))
    sessions = relationship("WebSession", backref="websession")


class WebSession(db.Model):
    __tablename__ = 'websession'

    session = Column(String(64), primary_key=True)
    lifetime = Column(Integer)
    user_uuid = Column(String(64), ForeignKey('user.uuid'))
    login_time = Column(DateTime)
    last_query_time = Column(DateTime)
    info = Column(String)


class Configura(db.Model):
    __tablename__ = 'configura'

    name = Column(String(32), primary_key=True)
    type = Column(String(8))
    value = Column(Binary, nullable=True)
    default_value = Column(Binary, nullable=True)
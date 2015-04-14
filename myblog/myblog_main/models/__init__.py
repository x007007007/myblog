from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import current_app
from uuid import uuid1
import datetime, time


db = SQLAlchemy()

class Commit(db.Model):
    __tablename__ = u'commit'
    uuid = db.Column(db.String(64), primary_key=True)
    article_uuid = db.Column(db.String(64), ForeignKey('article.uuid'))
    text = db.Column(db.String)


class Keyword(db.Model):
    __tablename__ = u'keyword'
    word = db.Column(db.String(32), primary_key=True)


class Article(db.Model):
    __tablename__ = u'article'
    uuid = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    commits = db.relationship("Commit", backref="commit")
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    @classmethod
    def new_uuid(cls):
        return "article_%s" % uuid1().hex

    def __init__(self, **kwargs):
        if 'uuid' not in kwargs:
            self.uuid = Article.new_uuid()
        if 'create_time' in kwargs:
            kwargs.pop('create_time')
        self.create_time = datetime.datetime.fromtimestamp(time.time())
        super(Article, self).__init__(**kwargs)





from flask_login import UserMixin, current_user
from flask import abort, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

rel = db.Table(
        'rel',
        db.Column('votecategory_id', db.Integer, db.ForeignKey('votecategory.id'), primary_key=True),
        db.Column('candidate_id', db.Integer, db.ForeignKey('candidate.id'), primary_key=True)
    )

class Users(db.Model, UserMixin):
    __name__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(40), default='null')
    last_name=db.Column(db.String(40), default='null')
    matriculation_number = db.Column(db.String(255), unique=True)
    private_key = db.Column(db.String(2555), unique=True)
    public_key = db.Column(db.String(2555), unique =True)
    is_admin = db.Column(db.Boolean, default=False)
    is_user = db.Column(db.Boolean, default=False)
    check = db.relationship()


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname=db.Column(db.String(40), default='null')
    first_name=db.Column(db.String(40), default='null')
    last_name=db.Column(db.String(40), default='null')
    rel = db.relationship('VoteCategory', secondary=rel, backref=db.backref('candidate_category', lazy='dynamic'))
 

class VoteCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), default='null')

class votedb.Model):
    id = db.Column(db.Integer, primary_key=True)
    voted_by = db.Column(db.Integer, db.Foreign('users.id'))
    voted_for = db.Column(db.Integer, db.Foreign('candidtate.id'))
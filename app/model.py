from flask_sqlalchemy import SQLAlchemy 
from app import app,db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user

from flask import session

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    email = db.Column(db.String(120),unique = True,nullable = False)
    image_file = db.Column(db.String(120),nullable = False , default = 'profile.jpg')
    password = db.Column(db.String(60),nullable = False)
    posts = db.relationship('Post',backref = 'rel', lazy = True)
    comments = db.relationship('Comment', backref = 'rep' ,lazy = True)
   
    
    def __repr__(self):
        return f"User('{self.username}' ,'{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(20))
    content= db.Column(db.Text(120))
    date = db.Column(db.DateTime , default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    post = db.relationship('Comment',backref = 'post', lazy = 'dynamic')
    def __repr__(self):
        return f"Post('{self.title}' ,'{self.content}', '{self.date}')"

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date = db.Column(db.DateTime , default = datetime.utcnow)
    name= db.Column(db.Text(120))
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Comment('{self.name}', '{self.date}')"
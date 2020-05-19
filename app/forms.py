from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from app.model import User,Post
from wtforms import ValidationError
from flask_login import current_user
from flask_wtf.file import FileAllowed,FileField

class RegistrationForm(FlaskForm):
    username = StringField('username',validators = [DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    confirm_password = PasswordField('Confirm password',validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_email(self,email):
            user = User.query.filter_by(email = email.data).first()

            if user:
                raise ValidationError('There is an account with that email')

    def validate_username(self,username):
        user= User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already taken')   

class LoginForm(FlaskForm):
    
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Sign In')

class UpdateAccount(FlaskForm):
    
    email = StringField('Email',validators = [DataRequired(),Email()])
    username = StringField('username',validators = [DataRequired(),Length(min=2,max=20)])
    picture = FileField('Update Picture',validators = [FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data!= current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username already taken')
    
    def validate_email(self,email):
        if email.data!= current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('There is an account with that email')

class PostForm(FlaskForm):
    title = StringField('Post Title')
    content = TextAreaField('Content')
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    name = TextAreaField('Comment',validators =[DataRequired()])
    submit = SubmitField('Post')
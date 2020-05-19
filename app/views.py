from app import app
from flask import render_template,redirect,url_for,flash,request,abort
from app.forms import RegistrationForm,LoginForm,UpdateAccount,PostForm,CommentForm
from app.model import User,Post,Comment
from app import app,db,bcrypt
from . import db
from flask_login import login_required,login_user,current_user,logout_user
from flask import session
import secrets
from flask_bcrypt import Bcrypt
import secrets
import os
from app import login_manager
from app.requests import quotes
import urllib.request,json

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




def upload_pic(save_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(save_picture.filename)

    picture_name = random_hex + f_ext
    load = os.path.join(app.root_path,'static/img',picture_name)

    save_picture.save(load)
    return picture_name

@app.route('/register',methods =["POST","GET"])
def register():
    if current_user.is_authenticated:
        flash(f'Already registered','danger')
        return redirect(url_for('main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username = username,email=email,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data} your Acoount has been created','success')
        return redirect(url_for('login'))
    return render_template('register.html',title = 'Register',form=form)

@app.route('/login',methods =["POST","GET"])
def login():
    if current_user.is_authenticated:
        flash(f'Already logged in','danger')
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        
        if user  and  bcrypt.check_password_hash(user.password,form.password.data):
             login_user(user,remember =form.remember.data)
             flash(f'Welcome  you  have succesfully logged into your account','success')
             return redirect(request.args.get('next') or url_for('main'))
             return redirect(url_for('main'))
        else:
             flash(f'Login unsucessful verify the email and password entered are correct','danger')

    return render_template('login.html',title = 'Login',form=form)


@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('main'))


@app.route('/profile',methods =["POST","GET"])


def profile():
     form = UpdateAccount()
     if form.validate_on_submit():
         if form.picture.data:
             picture_path = upload_pic(form.picture.data)
             current_user.image_file = picture_path
         current_user.username = form.username.data
         current_user.email = form.email.data
         db.session.commit()
         flash('account updated','success')
         return redirect(url_for('profile'))
     elif request.method == 'GET':
        #  user = User.query.filter_by()
         form.username.data = current_user.username
         form.email.data = current_user.email
     image_file = url_for('static',filename = 'img/'+ current_user.image_file)
     return render_template('profile.html',image_file=image_file,form=form)

@app.route('/')
@app.route('/home')
def main():
    posts = Post.query.all()
 
    data =quotes ()
    
    return render_template('index.html',posts=posts,data=data)



@app.route('/post/form',methods =["POST","GET"])
@login_required

def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        post = Post(title = title,content=content,rel = current_user)
        db.session.add(post)
        db.session.commit()
        flash('posted','success')
        return redirect(url_for('main'))
    return render_template('post.html',form = form,rel = current_user)





@app.route('/music')
@login_required
def music():
    posts = Post.query.all()
    print(posts)
    return render_template('music.html',posts=posts)


@app.route('/zendaya/<int:post_id>',methods =["POST","GET"])

@login_required

def zendaya(post_id):

    post = Post.query.get(post_id)
    comments = Comment.query.filter_by(post_id = post.id)
    form = CommentForm()
    if form.validate_on_submit():
        name= form.name.data
        comment = Comment(name = name,post_id = post.id,rep = current_user)
        db.session.add(comment)
        db.session.commit()
        
        return redirect(url_for('zendaya',post_id = post.id))


    return render_template('zendaya.html',post = post,comments = comments,form =form,rep = current_user)


@app.route('/bts/<int:post_id>',methods =["POST","GET"])

@login_required
def bts(post_id):

    post = Post.query.get(post_id)
    comments = Comment.query.filter_by(post_id = post.id)
    form = CommentForm()
    if form.validate_on_submit():
        name= form.name.data
        commen= Comment(name = name,post_id = post.id,rep = current_user)
        db.session.add(commen)
        db.session.commit()
        
        return redirect(url_for('bts',post_id = post.id))
    return render_template('bts.html',post = post,comments = comments,form =form,rep = current_user)

@app.route('/weekend/<int:post_id>',methods =["POST","GET"])

@login_required
def weekend(post_id):

    post = Post.query.get(post_id)
    comments = Comment.query.filter_by(post_id = post.id)
    form = CommentForm()
    if form.validate_on_submit():
        name= form.name.data
        commen= Comment(name = name,post_id = post.id)
        db.session.add(commen)
        db.session.commit()
        
        return redirect(url_for('weekend',post_id = post.id))
    return render_template('weekend.html',post = post,comments = comments,form =form)


@app.route('/zendaya<int:post_id>/comment/<int:comment_id>update',methods =["POST","GET"])

@login_required

def update_comment(post_id,comment_id):
    
    
       
    form = CommentForm()
    post = Post.query.get(post_id)
    comment= Comment.query.get(comment_id)
    if form.validate_on_submit():
            if comment.rep != current_user:
                flash('you cannot delete this post','danger')
                abort(403)
            post = Post.query.get(post_id)
            comment= Comment.query.get(comment_id)
            comment.name = form.name.data
            db.session.commit()
            flash('comment updated','success')
            return redirect(url_for('zendaya',post_id = post.id,comment_id = comment.id))
    elif request.method =='GET':
            form.name.data = comment.name
            
            
    return render_template('zendaya.html',form=form,post=post,comment=comment)  



@app.route('/zendaya<int:post_id>/comment/<int:comment_id>delete',methods =["POST","GET"])

@login_required

def delete_comment(comment_id,post_id):
    
    comment= Comment.query.get(comment_id)
    post= Comment.query.get(post_id)
    if comment.rep != current_user:
        flash('you cannot delete this post','danger')
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted','success')
    return redirect(url_for('music'))   
 
@app.route('/bts<int:post_id>/comment/<int:comment_id>delete',methods =["POST","GET"])

@login_required

def delete_commen(comment_id,post_id):
    comment= Comment.query.get(comment_id)
    post= Comment.query.get(post_id)
    if comment.rep != current_user:
        flash('you cannot delete this post','danger')
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted','success')
    return redirect(url_for('music'))   





@app.route('/bts<int:post_id>/comment/<int:comment_id>update',methods =["POST","GET"])

@login_required

def update_commen(post_id,comment_id):
    
    
       
    form = CommentForm()
    post = Post.query.get(post_id)
    comment= Comment.query.get(comment_id)
    if form.validate_on_submit():
            post = Post.query.get(post_id)
            commen= Comment.query.get(comment_id)
            comment.name = form.name.data
            db.session.commit()
            flash('comment updated','success')
            return redirect(url_for('bts',post_id = post.id,comment_id = comment.id))
    elif request.method =='GET':
            form.name.data = comment.name
            
            
    return render_template('bts.html',form=form,post=post,comment=comment)  











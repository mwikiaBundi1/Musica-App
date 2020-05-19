
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager,login_required,login_user,current_user
from flask_bcrypt import Bcrypt
from flask_mail import Mail,Message
from flask_simplemde import SimpleMDE

app = Flask(__name__)



app.config['SECRET_KEY'] = 'beb37ebec90537a85ac51a13567e276e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category ='info'

mail = Mail(app)
mail.init_app(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'lorrainekamanda@gmail.com'  
app.config["MAIL_PASSWORD"] = 'leilanjeri123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_PORT_TLS'] = 587

mail = Mail(app)
mail.init_app(app)

@app.route("/message")
def index():
   msg = Message('The Blog', sender = 'lorrainekamanda@gmail.com', recipients = ['lorrainekamanda@gmail.com'])
   msg.body = "Hello and Welcome to The Blog Thing where you get The to View Amazing Ideas "
   mail.send(msg)
   return render_template('index.html')



from app import views
from app import model
from app import requests
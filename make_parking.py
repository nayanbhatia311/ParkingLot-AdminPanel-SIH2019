from flask import Flask,render_template,url_for, request,redirect,flash,g
from functools import wraps
import json
import models 

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
	#form=LoginForm()
	return render_template("login.html")



@app.route("/",methods=['GET','POST'])
def submit():
	email=request.form.get('email')
	password=request.form.get('password')
	if email=='admin@parkinglot.com' and password=="admin123" and request.method=='POST':
		return redirect(url_for('adminpanel'))
	else:
		error="invlaid credentials"
		return redirect(url_for('home'))

	return render_template("login.html",error=error)
@app.route("/db_user")
def db_user():
    y = models.FromUser()
    fromuser = y.fromuser()
    return render_template("db_user.html",fromuser=fromuser)
@app.route("/create")
def create():
    return render_template("create.html")
@app.route("/db_comp")
def db_comp():
    
   
    z = models.PayandParking()
    payandpark = z.getPay()
    return render_template("db_comp.html",payandpark = payandpark)
@app.route("/home")
@app.route("/adminpanel")
def adminpanel():
    return render_template("index.html") 

@app.route("/active_users")
def active_users():
    x = models.UserModel()
    usermodel= x.getUser()
    return render_template("active_users.html",usermodel = usermodel)



@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/about")
def about():
    return render_template("about.html")
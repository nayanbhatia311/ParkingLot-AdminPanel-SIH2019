from flask import Flask,render_template,url_for, request,redirect,flash,g
from functools import wraps
import json
flag=False
email=None
password=None
app= Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
def home():
	#form=LoginForm()
	return render_template("login.html")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if flag==False:
            return redirect(url_for('home', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/",methods=['GET','POST'])
def submit():
	email=request.form.get('email')
	password=request.form.get('password')
	if email=='admin@parkinglot.com' and password=="admin123" and request.method=='POST':
		flag=True
		return redirect(url_for('adminpanel'))
	else:
		error="invlaid credentials"
		return redirect(url_for('home'))

	return render_template("login.html",error=error)


@app.route("/adminpanel")
#@login_required
def adminpanel():
	flash('You were successfully logged in')
	database=json.loads(open("C:\\Users\\pp.json").read())
	print(database)
	return render_template("adminpanel.html",database=database)




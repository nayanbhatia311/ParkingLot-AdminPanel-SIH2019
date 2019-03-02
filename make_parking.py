from flask import Flask,render_template,url_for, request,redirect,flash

import json
import models 



# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if  is None :
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function


print(models.session)
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route("/")
#@login_required
def home():
	#form=LoginForm()
	return render_template("login.html")


@app.route('/logout')
def logout():
	models.session=False
	return redirect(url_for('home'))



@app.route("/",methods=['GET','POST'])
def submit(): 
	email=request.form.get('email')
	password=request.form.get('password')
	if email=='admin@mahindra.com' and password=="admin123" and request.method=='POST':
		models.session=True
		return redirect(url_for('adminpanel'))
	else:
		error= "invalid credentials"
		return render_template("login.html",error=error)

@app.route("/db_user", methods=['POST','GET'])
def db_user():
	if not models.session:
		return redirect (url_for('home'))
	else:
		y = models.FromUser()
		fromuser = y.fromuser()
		if request.method == 'POST':
			value = request.form.get('loop')
			print(value)
			remove = models.Deletion(value)
			remove.dele()
		return render_template("db_user.html",fromuser=fromuser)

# @app.route('/c',methods=['POST','GET'])
# def c():
#     form = forms.ReusableForm()
#     if request.method == 'POST':
#         if form.validate() == False:
#             flash('All fields are required.')
#             return render_template('create.html', form = form)
#         elif form.validate() == True:
#             name = request.form.get('name')
#             address1 = request.form.get('address1')
#             address2 = request.form.get('address2')
#             city =  request.form.get('city')
#             latitude =  request.form.get('latitude')
#             longitude =  request.form.get('longitude')
#             capacity =  request.form.get('capacity')
#             days =  request.form.get('days')
#             restrictions =  request.form.get('restriction')
#             category = request.form.get('category')
#             timing = request.form.get('timing')
#             chargesperhour =  request.form.get('chargesperhour')
#             data =  models.CreateLot(name,address1,address2,city,latitude,longitude,capacity,days,restrictions,category,timing,chargesperhour)
#             data.insert()
#             return render_template('db_comp.html')
#     return render_template('db_comp.html')


@app.route("/create", methods=['POST','GET'])
def create():
	if not models.session:
		return redirect (url_for('home'))
	else:
		name = request.form.get('name')
		address1 = request.form.get('address1')
		address2 = request.form.get('address2')
		city =  request.form.get('city')
		latitude =  request.form.get('latitude') 
		longitude =  request.form.get('longitude')
		capacity =  request.form.get('capacity')
		days =  request.form.get('days')
		restrictions =  request.form.get('restriction')
		category = request.form.get('category')
		timing = request.form.get('timing')
		chargesperhour =  request.form.get('chargesperhour')
		print(name,address1,address2,city,latitude,longitude,capacity,days,restrictions,category,timing,chargesperhour)
		if request.form.get('submit') == '1':
			print(name,address1,address2,city,latitude,longitude,capacity,days,restrictions,category,timing,chargesperhour)
			data =  models.CreateLot(name,address1,address2,city,latitude,longitude,capacity,days,restrictions,category,timing,chargesperhour)
			data.insert()
		# x = {
		#     "status" : 200
		# }
		return render_template("create.html")

@app.route("/db_comp",methods=['POST','GET'])
def db_comp():
	if not models.session:
		return redirect (url_for('home'))
	else:
		z = models.PayandParking()
		payandpark = z.getPay()
		if request.method == 'POST':
			value = request.form.get('del')
			print("del obj"+value)
			remove = models.Deletionfrompay(value)
			response = remove.dele()
		# return render_template("db_user.html",fromuser=fromuser)

		return render_template("db_comp.html",payandpark = payandpark)

@app.route("/home")
@app.route("/adminpanel")
def adminpanel():
	if not models.session:
		return redirect (url_for('home'))
	else:
		return render_template("index.html") 

@app.route("/active_users")
def active_users():
	if not models.session:
		return redirect (url_for('home'))
	else:
		x = models.UserModel()
		usermodel= x.getUser()
		return render_template("active_users.html",usermodel = usermodel)



@app.route("/team")
def team():
	if not models.session:
		return redirect (url_for('home'))
	else:
		return render_template("team.html")

@app.route("/about")
def about():
	if not models.session:
		return redirect (url_for('home'))
	else:
		return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
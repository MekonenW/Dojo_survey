from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key= "KeepItSecret"

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_users():	
	session['name']= request.form['name']
	session['comment']= request.form['comment']
	session['language']= request.form['language']
	session['location']= request.form['location']

	
	if len(session['name'])>1 and len(session['comment']) >1 and len(session['comment'])<120:
		return render_template('another.html')

	if len(request.form['name']) <1:
		flash("Name cannot be empty!")
	else: 
		flash("Welcome to my page {}".format(request.form['name']))
		
	if len(request.form['comment']) <1:
		flash("Comment field cannot be empty")
	if len(request.form['comment']) >120:
		flash("Your comment is too long.")
	else:
		flash('Thank you for your feedback!')
		return redirect('/')

	

app.run(debug=True)

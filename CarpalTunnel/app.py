from flask import Flask
from flask import render_template
from flask import request
from firebase import firebase
from flask import json

firebase = firebase.FirebaseApplication('https://carpal-tunnel.firebaseio.com', None)
result = firebase.get('/users', None)
print result

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']

	new_user = _name + ' ' + _email + ' ' + _password

	print 'signing up'

	if _name and _email and _password:
		result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER' : 'VERY FANCY'})
		print 'hi'#return json.dumps({'html':'<span>All fields good !!</span>'})
    
if __name__ == "__main__":
	app.run()
#https://carpal-tunnel.firebaseio.com/
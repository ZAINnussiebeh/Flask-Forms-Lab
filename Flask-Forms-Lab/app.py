from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "mahmoud"
password = "mahmoud"
facebook_friends=["antony","farid","mahmoud", "lour", "dina", "rooa"]


@app.route('/', methods=['GET','POST']) 
def login():
  if request.method == 'GET':
        return render_template('login.html')
  else:
        if username==request.form['username'] and password==request.form['password']:
        	return render_template('home.html', facebook_friends=facebook_friends)
        else:
        	return render_template('login.html')


@app.route('/friend_exists/<string:name>' ,methods=['GET','POST'])
def hello_name_route(name):
	if name in facebook_friends:
			return render_template('friend_exists.html', exists=True)
	return render_template('friend_exists.html',exists =False)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
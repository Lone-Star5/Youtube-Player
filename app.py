
from flask import Flask
from flask import render_template, redirect, request, session,url_for,Response,request,send_file
from urllib import parse as urlparse
import pytube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)

playlist = False

@app.route("/", methods=['POST','GET'])
def index():
	if request.method == 'POST':
		url= request.form['content']
		if(len(url) == 0 ):
			return render_template("index.html")
		else: 
			url_data=urlparse.urlparse(url)
			query = urlparse.parse_qs(url_data.query)
			video = query["v"][0]
			return render_template('index.html',video=video,playlist = playlist)
	else:
		return render_template("index.html",playlist=playlist)

@app.route("/download",methods=['POST','GET'])
def download():
	if request.method == 'POST':
		url= request.form.get("content", True)
		print (url)
	return redirect("/")

<<<<<<< HEAD
=======
@app.route("/playlist", methods = ['GET'])
def createlist():
	global playlist
	playlist = True
	return redirect("/")

@app.route("/playlist/close", methods = ['GET'])
def closelist():
	global playlist
	playlist = False
	return redirect("/")	
>>>>>>> upstream/master

if __name__ == "__main__":
	app.run(debug=True)


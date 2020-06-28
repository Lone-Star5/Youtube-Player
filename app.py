
from flask import Flask
from flask import render_template, redirect, request, session,url_for,Response,request,send_file
from urllib import parse as urlparse
import pytube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)

playlist = False
links = []

@app.route("/", methods=['POST','GET'])
def index():
	if request.method == 'POST':
		if(request.form.get('play',False) == "Play"):
			url= request.form['content']
			if(len(url) == 0 ):
				return render_template("index.html")
			else: 
				url_data=urlparse.urlparse(url)
				query = urlparse.parse_qs(url_data.query)
				video = query["v"][0]
				return render_template('index.html',video=video,playlist = playlist, links = links)
		if(request.form.get('delete', False)=='Delete'):
			links.remove(request.form['content'])
			return render_template('index.html',playlist = playlist, links = links)
		
		if(request.form.get('download', False)=='Download'):
			url= request.form['content']
			link = url
			yt = pytube.YouTube(link)
			stream = yt.streams.first()
			return send_file(stream.download(),as_attachment=True)

	else:
		return render_template("index.html",playlist=playlist, links = links)

@app.route("/new", methods = ['POST'])
def create():
	if request.method == 'POST':
		url = request.form['content']
		if(len(url)==0):
			return redirect("/")
		else:
			global links
			links.append(url);
			return redirect("/")

# @app.route("/download",methods=['POST','GET'])
# def download():
# 	if request.method == 'POST':
# 		url= request.form.get("content", True)
# 		return url
# 	return redirect("/")

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

if __name__ == "__main__":
	app.run(debug=True)



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
		link = url
		yt = pytube.YouTube(link)
		stream = yt.streams.first()	
		return send_file(stream.download(),as_attachment=True)
	return redirect("/")

@app.route("/playlist", methods = ['GET'])
def list():
	global playlist
	playlist = True
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)





	# https://www.youtube.com/watch?v=Z1RJmh_OqeA


	# <iframe width="560" height="315" src="https://www.youtube.com/embed/Z1RJmh_OqeA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
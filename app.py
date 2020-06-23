
from flask import Flask
from flask import render_template, redirect, request, session,url_for,Response,request

from download import stream

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
	if request.method == 'POST':
		link= request.form['content']
		return link
	else:
		return render_template("index.html")

@app.route("/download",methods=['POST','GET'])
def download():
	if request.method == 'POST':
		stream.download("../Downloads")
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
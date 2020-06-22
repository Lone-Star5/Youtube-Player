from flask import Flask
from flask import render_template, redirect, request, session,url_for,Response

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
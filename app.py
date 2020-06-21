from flask import Flask,render_template
import pytube

app = Flask(__name__)

def down():
	link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	stream.download("../Downloads")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/download")
def download():
	# Run download.py file
	down();
	return "Done"

if __name__ == "__main__":
	app.run(debug=True)

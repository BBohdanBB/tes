from flask import Flask, render_template
icc = Flask(__name__)

@MyApp.route("/")
def hello():
	return render_template('index.html')

if __name__ == "__main__":
	icc.run()

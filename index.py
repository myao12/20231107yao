from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():

	homepage = "<h1>資工四B 410903652 楊明耀的求職資訊</h1>"

	homepage += "<a href=/about>我的個人簡介</a><br>"
	
	homepage += "<a href=/today>職涯測驗結果</a><br>"

	homepage += "<a href=/welcome>求職履歷自傳</a><br>"

	homepage += "<a href=/mis>MIS相關工作介紹</a><br>"

	return homepage

@app.route("/about")

def about():
	return render_template("aboutme.html")

@app.route("/today")

def today():

	return render_template("today.html")

@app.route("/welcome")

def welcome():
	
	return render_template("welcome.html")

@app.route("/mis")

def course():
	return render_template("mis.html")




#if __name__ == "__main__":

#	app.run()
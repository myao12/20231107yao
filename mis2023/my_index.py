from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資工四B 410903652 楊明耀的求職資訊</h1>"
    homepage += "<a href=/about>我的個人簡介</a><br>"
    homepage += "<a href=/today>職涯測驗結果</a><br>"
    homepage += "<a href=/welcome?nick=myyang>求職履歷自傳</a><br>"
    homepage += "<a href=/mis>MIS相關工作介紹</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

if __name__ == "__main__":
   app.run()
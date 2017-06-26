from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

username = ""
password = ""
email = ""



@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]




    return render_template("home-page.html", username=username, email=email)

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form['username']
    return render_template("welcome-page.html", username=username, title="Welcome!")

app.run()

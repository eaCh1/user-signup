from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template("home-page.html")

@app.route("/validate", methods=['POST'])
def validate_info():
    username = ""
    password = ""
    verify = ""
    email = ""

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    match_error = ""

    if not is_empty_username():
        username_error = "That's not a valid username"
    if not is_empty_password():
        password_error = "That's not a valid password"
    if not is_empty_verify():
        verify_error = "That's not a valid password"

    if not is_valid_username():
        username_error = "That's not a valid username"
    if not is_valid_email():
        email_error = "That's not a valid email"
    if not is_valid_password():
        password_error = "That's not a valid password"

    if not do_passwords_match():
        verify_error = "Passwords don't match"

    if not username_error and not password_error and not match_error:
        return render_template("welcome-page.html",
                                username = request.form["username"],
                                title = "Welcome!")
    else:
        return render_template("home-page.html",
                                username = request.form["username"],
                                email = request.form["email"],
                                usernameerror = username_error,
                                passworderror = password_error,
                                verifyerror = verify_error,
                                emailerror = email_error)


def is_valid_username():
    username = request.form["username"]
    if 21 >= len(username) >= 3:
        if not " " in username:
            return True
    return False

def is_valid_email():
    email = request.form["email"]
    if 21 >= len(email) >= 3:
        if "@" in email and "." in email:
            if not " " in email:
                return True
    return False

def is_valid_password():
    password = request.form["password"]
    if 21 >= len(password) >= 3:
        if not " " in password:
            return True
    return False

def is_empty_username():
    username = request.form["username"]
    if username != "":
        return True
    return False

def is_empty_password():
    password = request.form["password"]
    if password != "":
        return True
    return False

def is_empty_verify():
    verify = request.form["verify"]
    if verify != "":
        return True
    return False

def do_passwords_match():
    password = request.form["password"]
    verify = request.form["verify"]
    if password == verify:
        return True
    return False

app.run()

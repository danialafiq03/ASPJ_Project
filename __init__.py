from flask import Flask, render_template, render_template_string, request, make_response, redirect, url_for
import os
import pickle
from base64 import b64encode, b64decode
from User import User

app = Flask(__name__)
app.secret_key = 'secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        email = request.form['email']
        return email

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        user_obj = User(email)
        response = make_response(redirect(url_for("welcome")))
        response.set_cookie("uid", b64encode(pickle.dumps(user_obj)))
        return response
    else:
        if "uid" in request.cookies:
            return redirect(url_for("welcome"))
        return render_template('login.html')

@app.route('/logout')
def logout():
    # session.pop("email", None)
    response = make_response(redirect(url_for('login')))
    response.delete_cookie("uid")
    return response

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/index")
def index():
    search = request.args.get('search')

    template = '''
        {}
    '''.format(search)
    return render_template_string(template)


@app.route('/welcome')
def welcome():
    user_obj = request.cookies.get("uid")
    if user_obj:
        return "Hey there! {}" .format(pickle.loads(b64decode(user_obj)))
    else:
        return redirect(url_for("login"))

# @app.route('/welcome')
# def welcome():
#     email = session["email"]
#     if email:
#         return render_template("welcome.html", email=email)
#     else:
#         return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)

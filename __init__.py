from flask import Flask, render_template, render_template_string, request, make_response, redirect, url_for, session

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
        session["email"] = email
        return redirect(url_for("welcome"))

        # response = make_response(redirect(url_for("getcookie")))
        # response.set_cookie("email", email)
        # return response
    else:
        if "email" in session:
            return redirect(url_for('welcome'))
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("email", None)
    return redirect(url_for("login"))

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
   email = session["email"]
   if email:
       return render_template("welcome.html", email=email)
   else:
       return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)

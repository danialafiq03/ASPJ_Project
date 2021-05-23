from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        email = request.form['email']
        return email

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    email = request.form['email']
    return render_template('welcome.html', email=email)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/index")
def index():
    search = request.args.get('search')

    template = '''
        <p>Hello World</p>
        {}
    '''.format(search)

    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)

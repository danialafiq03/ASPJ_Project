from flask import Flask, render_template, render_template_string, request, session, Response
from flask_socketio import SocketIO, send
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.before_request
def before_request():
    random_num = random.randint(0, 10000)
    session['guest_id'] = random_num
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

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

@app.route('/chat')
def chat():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    if msg == "has connected!":
        send('Guest #' + str(session['guest_id']) + ' ' + msg, broadcast=True)
    else:
        send('Guest #' + str(session['guest_id']) + ': ' + msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

from flask import Flask

app = Flask(__name__)

#MAIN PAGE OF THE APPLICATION
@app.route("/")
def index():
    return '<h1>SKARABI</h1>'

#DYNAMIC ROOT
@app.route('/user/<name>')
def user(name):
    return'<h1>Hello,%s!</h1>'%name


if __name__ == '__main__':
    app.run(debug=True)
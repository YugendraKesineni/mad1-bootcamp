from flask import Flask

app = Flask(__name__) #__name__ checks the current file.

@app.route("/")
def index():
    return "<h1> Hello, World !</h1>"


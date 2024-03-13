from flask import Flask

app = Flask(__name__) #__name__ checks the current file.

@app.route("/greet/charlie")
def index():
    return "<h1> Hello, Word !</h1>"

app.run(debug=True)
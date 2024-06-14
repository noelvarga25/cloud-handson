from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hi! My name is Noel Varga. I am a Cloud Computing Expert</h1></body></html>\n"
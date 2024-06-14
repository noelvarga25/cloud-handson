from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi! My name is Noel Varga. I am a Cloud Computing Expert\n"
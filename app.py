from flask import Flask
app = Flask(__name__)

@app.route("/POC")
def hello():
    return "<!-- PoC by MikeTheTortoise24 -->"

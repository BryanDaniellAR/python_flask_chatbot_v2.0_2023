from flask import Flask,render_template
from src.Routes.route import botRoute

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template("index.html")

botRoute(app)

if __name__ == "__main__":
    app.run('0.0.0.0')
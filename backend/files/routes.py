from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/home")
def home():
    return "Hello! This is the main page"

@app.route("/add",methods=["POST","GET"])
def add_info():
    description = request.json['description']
    images = request.json['images']
    print(description)
    print(images)
    return description

if __name__ == "__name__":
    app.run()
    
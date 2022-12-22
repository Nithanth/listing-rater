from flask import Flask, request

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello! This is the main page"

@app.route("/add",methods=["POST","GET"])
def add_info():
    description = request.json['description']
    print(description)
    return description

# @app.route("/add", methods=["POST"], strict_slashes=False)
# def add_articles():
#     title = request.json['title']
#     body = request.json['body']

if __name__ == "__name__":
    app.run()
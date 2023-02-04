from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/add",methods=["POST"])
def add_info():
    description = request.json['description']
    images = request.json['images']
    
    return description

@app.route("/generate",methods=["POST"])
def generate_description():
    address = request.json['address']
    print(address)
    print(type(address))
    return address

if __name__ == "__name__":
    app.run()
    
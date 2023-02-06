from flask import Flask, request
from flask_cors import CORS
import master

app = Flask(__name__)
cors = CORS(app)

@app.route("/add",methods=["POST", "GET"])
def add_info():
    description = request.json['description']
    images = request.json['images']
    image_results = master.check_images(images)
    description_results = master.check_description(description)
    response = [[description_results], [image_results]]
    return response

@app.route("/generate",methods=["POST"])
def generate_description():
    address = request.json['address']
    platform = request.json['platform']
    generated_description = master.auto_generate(platform, address)
    response = [generated_description]
    return response

if __name__ == "__name__":
    app.run()
    
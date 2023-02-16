from flask import Flask, request, jsonify
from flask_cors import CORS
import master

app = Flask(__name__)
cors = CORS(app)

@app.route("/add",methods=["POST"])
def add_info():
    # description = request.json['description']
    images = request.json['images']
    # print(images)
    image_data = master.image_feedback(images)
    # description_results = master.check_description(description)
    # print(image_data)
    response = jsonify({"response": image_data})
    print(response)
    # print(response)
    return response

@app.route("/generate",methods=["POST"])
def generate_description():
    address = request.json['address']
    platform = request.json['platform']
    generated_description = master.auto_generate(platform, address)
    response = [generated_description]
    return response

if __name__ == "__main__":
    app.run()
    
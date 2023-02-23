from flask import Flask, request, jsonify
from flask_cors import CORS
import master

app = Flask(__name__)
cors = CORS(app)

@app.route("/evaluate_images",methods=["POST"])
def add_info():
    images = request.json['images']
    image_data = master.image_feedback(images)
    print("image feedback:",image_data)
    response = jsonify({"response": image_data})
    print("jsonified response:",response)
    return response

@app.route("/evaluate_description",methods=["POST"])
def evaluate_description():
    description = request.json['description']
    description_results = master.description_feedback(description)
    response = jsonify({"response": description_results})
    print(response)
    return response

@app.route("/generate",methods=["POST"])
def generate_description():
    address = request.json['address']
    bedroom_count = request.json['bedroom_count']
    bathroom_count = request.json['bathroom_count']
    # amenities = request.json['amenities']
    platform = 'openai'
    generated_description = master.auto_generate(platform, address)
    response = [generated_description]
    return response

if __name__ == "__main__":
    app.run()
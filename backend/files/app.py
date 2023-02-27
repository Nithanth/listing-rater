from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import master

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String(200), nullable=False)
    bathroom_count = db.Column(db.Float(3), nullable=False)
    bedroom_count = db.Column(db.Float(3), nullable=False)
    amenities = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/generate", methods=["POST"])
def generate_description():
    address = request.json['address']
    amenities = request.json['amenities']
    bedroom_count = request.json['bedroom_count']
    bathroom_count = request.json['bathroom_count']
    platform = 'openai'

    # generate description
    # generated_description = master.generate_description(
    #     platform, address, amenities, bedroom_count, bathroom_count)
    generated_description = "testRESULT"
    print(generated_description)

    # commit input and response data to database
    data_entry = Data(address=address,bedroom_count=bedroom_count,bathroom_count=bathroom_count,amenities=amenities,result=generated_description)
    db.session.add(data_entry)
    db.session.commit()

    with app.app_context():
        entries = Data.query.all()
        for entry in entries:
            print(f"---- DB ENTRY ----")
            print(f"Address: {entry.timestamp}")
            print(f"Address: {entry.address}")
            print(f"Bedroom count: {entry.bedroom_count}")
            print(f"Bathroom count: {entry.bathroom_count}")
            print(f"Amenities: {entry.amenities}")
            print(f"Result: {entry.result}")

    # return response
    response = [generated_description]
    return response


@app.route("/evaluate_images", methods=["POST"])
def add_info():
    images = request.json['images']
    image_data = master.image_feedback(images)
    print("image feedback:", image_data)
    response = jsonify({"response": image_data})
    print("jsonified response:", response)
    return response


@app.route("/evaluate_description", methods=["POST"])
def evaluate_description():
    description = request.json['description']
    description_results = master.description_feedback(description)
    response = jsonify({"response": description_results})
    print(response)
    return response




if __name__ == "__main__":
    db.create_all()
    app.run()
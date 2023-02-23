from flask import Flask, request, jsonify
from flask_cors import CORS
import master

app = Flask(__name__)
cors = CORS(app)


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


@app.route("/generate", methods=["POST"])
def generate_description():
    address = request.json['address']
    amenities = request.json['amenities']
    bedroom_count = request.json['bedroom_count']
    bathroom_count = request.json['bathroom_count']
    platform = 'openai'
    generated_description = master.generate_description(
        platform, address, amenities, bedroom_count, bathroom_count)
#     generated_description = """
# About this space
# Enjoy a luxe all-suite layout, a sleek full kitchen, and stunning Gulf views on your private covered balcony! As part of the Origin Beach Resort, this modern 1BR retreat that sleeps 6 features outdoor pool and hot tub, fitness center, game room and a very large common area observation deck with breathtaking gulf views. This BEAUTIFULLY RENOVATED / 1 bed 1 bath condo has been completely renovated to meet the upscale taste of the owner. Renovations include: Refurbished kitchen cabinets with new hardware, completely renovated bathroom with a walk-in tiled shower and double sink vanity, wood look tile throughout the main living area and master bedroom, freshly painted, upgraded furniture, new hot water heater in 2021 and is an ABSOLUTE MUST SEE!!. Origin at Seahaven has unsurpassed amenities which include a gulf view pool & hot tub, sunrise and sunset observation decks, grilling & gathering decks, fitness room, movie theater and game room. Origins FANTASTIC beach location is steps to Pier Park, shopping and dining
# Other things to note Please be aware that there will be NO refunds for Wifi issues as it’s not guaranteed at the beach. If reliable wifi is a must you are welcome to bring your own internet hotspot.
#     """
    print(generated_description)
    response = [generated_description]
    return response


if __name__ == "__main__":
    app.run()

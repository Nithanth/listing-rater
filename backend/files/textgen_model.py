import os
import openai
import cohere
from secrets_vault import COHERE_API_KEY, OPENAI_API_KEY


def generate_property_description_openai(address, amenities, bedroom_count, bathroom_count):
    print("in function")
    print(address, amenities, bedroom_count, bathroom_count)
    MODEL = "text-davinci-003"
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model=MODEL,
        prompt=f"Write an AirBNB description for a property located at {address}. The address is: {address}. It has {bedroom_count} bedrooms and {bathroom_count} bathrooms. The amenities include {amenities}. Start the introduction paragraph with a catchy line to draw attention to our property. Include the bedroom and bathroom information. Also, write a sentence for each amenity to showcase them! This paragraph should be between 3-7 sentences. If there's more than 3 amenities, focus on the top 3 most appealing ones. In the second paragraph, focus on describing the appeal of the area. Don't discuss nearby attractions, shopping, restaurants, but from a vacation-standpoint, describe the picture-esque beauty of the area. This paragraph should be between 3-4 sentences and provide guests an alluring image of the area. In the final paragraph, include names of nearby popular restaurants and attractions and how far they are from the home. Limit restaurants and attractions to a max of 3. Wrap up this paragraph with an appropriate line to wrap up the entire description. Don't explicitly include the address in the description. Don't reuse adjectives. Use at least 250 words.",
        max_tokens=1000,
        temperature=0.5
    )
    # response = requests.post("https://api.openai.com/v1/engines/{}/jobs".format(MODEL),
    #   headers={
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {API_KEY}"
    #   },
    #   json={
    #     "prompt": prompt,
    #     "max_tokens": 2048,
    #     "temperature": 0.5,
    #   }
    # )

    return response["choices"][0]["text"]


def generate_property_description_cohere(address, amenities, bedroom_count, bathroom_count):
    MODEL = 'command-xlarge-nightly'
    co = cohere.Client(COHERE_API_KEY)
    # co_prompt=f"Write an Airbnb-like description that describes the property and amenties really well to customers for this address: {address}"
    imagery_prompt = f"I am writing an AirBNB description for a property located in: {address}. Give me a paragraph to describe the beauty of the surrounding area to potential short-term rental guests. Use vivid imagery and location-specific word choice. Do not describe the amenities of a specific property."
    # amenity_prompt = f"Give me a cool way to describe : {address}"
    response = co.generate(
        model=MODEL,
        prompt=imagery_prompt,
        max_tokens=400,
        temperature=0.5,
        stop_sequences=["--"])
    return response.generations[0].text


# address = input("Enter an address: ")
# address = input("Enter a location: ")
# property_description = generate_property_description_openai(address)
# print("Description of the property:")
# print(property_description)
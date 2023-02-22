import os
import openai
import cohere
from secrets_vault import COHERE_API_KEY, OPENAI_API_KEY

def generate_property_description_openai(address):
    
    MODEL = "text-davinci-002"
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
    model=MODEL,
    prompt=f"Write an Airbnb-like description that describes the property and amenties really well to customers for this address: {address}",
    max_tokens=2048,
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

def generate_property_description_cohere(address):
    MODEL = 'command-xlarge-nightly'
    co = cohere.Client(COHERE_API_KEY)
    # co_prompt=f"Write an Airbnb-like description that describes the property and amenties really well to customers for this address: {address}"
    imagery_prompt = f"Give me 5 examples of imagery to describe the beauty of the area that the following address is in, limit each example to 25 words. The address of the area is: {address}"
    # amenity_prompt = f"Give me a cool way to describe : {address}"
    response = co.generate(  
        model=MODEL,  
        prompt = imagery_prompt,  
        max_tokens=400,  
        temperature=0.5,  
        stop_sequences=["--"])
    return response.generations[0].text


# address = input("Enter an address: ")
# property_description = generate_property_description_cohere(address)
# print("Description of the property:")
# print(property_description)
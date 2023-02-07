import os
import openai
import cohere
from secrets import COHERE_KEY, OPENAI_KEY

def generate_property_description_openai(address):
    
    MODEL = "text-davinci-002"
    openai.api_key = OPENAI_KEY
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
    co = cohere.Client(COHERE_KEY)
    co_prompt=f"Write an Airbnb-like description that describes the property and amenties really well to customers for this address: {address}"
    response = co.generate(  
        model=MODEL,  
        prompt = co_prompt,  
        max_tokens=400,  
        temperature=0.5,  
        stop_sequences=["--"])
    return response.generations[0].text


address = input("Enter an address: ")
property_description = generate_property_description_cohere(address)
print("Description of the property:")
print(property_description)
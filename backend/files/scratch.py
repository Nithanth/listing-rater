import requests

def generate_property_description(address):
    API_KEY = "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"
    MODEL = "text-davinci-002"
    prompt = f"Describe the property at address: {address}"

    response = requests.post("https://api.openai.com/v1/engines/{}/jobs".format(MODEL),
      headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
      },
      json={
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0.5,
      }
    )

    if response.status_code != 200:
        print(response.status_code)
        raise ValueError("Failed to generate description")

    description = response.json()["choices"][0]["text"]
    return description

address = input("Enter an address: ")
property_description = generate_property_description(address)
print("Description of the property:")
print(property_description)
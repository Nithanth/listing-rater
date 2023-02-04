import requests

url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
url2 = "https://api.openai.com/v1/completions"

query = {
    "prompt": "Write me an AirBNB listing description for a short-term rental at 6024 Almelo Drive, Round Rock, Texas.",
    "temperature": 0.5,
    "max_tokens": 100,
    "top_p": 1,
    "n": 1,
    "stream": False,
    "model": 'text-davinci-003'
}

api_key = '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'

response = requests.post(url2, json=query, headers={
  "Content-Type": "application/json",
  "Authorization": api_key
})

if response.status_code == 200:
    completions = response.json()["choices"]
    answer = completions[0]["text"]
    print(answer)
else:
    print("Request failed")
    print(response.status_code)

# curl https://api.openai.com/v1/completions \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer YOUR_API_KEY" \
# -d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
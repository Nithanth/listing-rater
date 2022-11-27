from flask import Flask

app = Flask(__name__)

# members API route
@app.route("/members")
def members():
    return {"members":["a1","a2","a3"]}


if __name__ == "__main__":
    app.run(debug=True)
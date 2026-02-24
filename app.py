from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"


def get_random_fact():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["text"]
    except Exception:
        return "Could not fetch the fact. Try again!"


@app.route("/", methods=["GET", "POST"])
def home():
    fact = None
    if request.method == "POST":
        fact = get_random_fact()

    return render_template("index.html", fact=fact)


if __name__ == "__main__":
    app.run(debug=True)
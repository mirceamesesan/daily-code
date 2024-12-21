import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_time_entries():
    """Retrieving all our time entries from the database"""
    # response = requests.get(url="http://localhost:8000")
    # print(response.json())
    print("Retrieving time entries...")


@app.route("/")
def home():
    get_time_entries()
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

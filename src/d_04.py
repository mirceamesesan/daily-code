import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_time_entries():
    """Retrieving all our time entries from the database"""
    response = requests.get(url="http://localhost:8000/entries/")
    return response.json()


@app.route("/")
def home():
    entries = get_time_entries()
    total = sum([float(entry["duration"]) for entry in entries])
    print(f"Entries: {len(entries)}")
    return render_template("home.html", entries=entries, total_duration=total)


if __name__ == "__main__":
    app.run(debug=True)

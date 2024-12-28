import requests
from flask import Flask, render_template, request, redirect
from services.sudoku import Sudoku

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


@app.route("/add_entry", methods=["POST"])
def add_entry():
    data = {
        "description": request.form["description"],
        "duration": request.form["duration"],
    }
    response = requests.post(url="http://localhost:8000/entry/", json=data)
    print(response.status_code)
    return redirect("/")


@app.route("/sudoku", methods=["GET", "POST"])
def sudoku():
    board = Sudoku(120).generate_board()
    return render_template("sudoku.html", board=board)

if __name__ == "__main__":
    app.run(debug=True)

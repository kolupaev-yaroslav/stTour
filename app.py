from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/departures/<departure>/")
def departure(departure):
    return render_template("departure.html")

@app.route("/tours/<id>/")
def tour(id):
    return render_template("tour.html")


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)


@app.route('/')
def index():

    response        = urllib.request.urlopen('http://api.fixer.io/latest?base=AUD')
    data  = json.load(response)

    date         = data["date"]
    base           = data["base"]
    rates = data["rates"]
    records = []

    for key in rates:
        record_tuple = (date, base, key,rates[key])
        records.append(record_tuple)

    return render_template('index.html', records=records)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)

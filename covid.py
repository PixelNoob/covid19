import datetime
from flask import Flask, render_template
import requests as r
import json
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

@app.route('/')
@app.route('/home')
def home():
    ts = datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')
    with open('/scripts/cases.json') as json_file: # Put the right path to cases.json file
        data = json.load(json_file)
    confirmed = 0
    for cases in data:
        confirmed = confirmed + int(cases['confirmed'])
    deaths = 0
    for cases in data:
        deaths = deaths + int(cases['deaths'])
    rows= {}
    for cases in data:
        rows.update({ cases['country']: (cases['confirmed'], cases['deaths'])})
    return render_template("list.html",rows = rows, ts = ts, confirmed = confirmed, deaths = deaths )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)

# app.run(host='0.0.0.0', port=80, debug=True)

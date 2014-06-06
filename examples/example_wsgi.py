#!/usr/bin/python
# coding: utf8

from flask import Flask, json, Response
import geocoder

app = Flask(__name__)

@app.route('/geocoder/<location>', methods=['POST','GET'])
def geocode(location):
    g = geocoder.google(location)
    resp = json.dumps(g.json, ensure_ascii=False, indent=' '*2)
    mimetype = "application/json; charset=UTF-8"

    return Response(response=resp, status=200, mimetype=mimetype)

if __name__ == "__main__":
    app.run(debug=True)
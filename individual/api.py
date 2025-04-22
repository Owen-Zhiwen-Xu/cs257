#!/usr/bin/env python3
'''
    api.py
    Owen Xu, 21 April 2025
'''
import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)

@app.route('/<district>')
def get_crimes(district):
    crimes = []
    area_name = 5
    crime_type = 9
    with open('data/Crime_Data_from_2020_part.csv') as f:
        reader = csv.reader(f)
        for crime_row in reader:
            if crime_row[area_name] == district:
                crimes.append(crime_row[crime_type])
    return json.dumps(crimes)

@app.route('/')
def hello():
    return 'Hello, Welcome to Crime Data.'

@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A API to get crime data')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
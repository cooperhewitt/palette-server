#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import palette

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/extract', methods=['GET'])
@cross_origin(methods=['GET'])
def extract():

    path = flask.request.args.get('path')

    rsp = palette.get_colours(path)
    return flask.jsonify(**rsp)

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)

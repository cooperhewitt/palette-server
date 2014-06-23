#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

import cooperhewitt.swatchbook
import roygbiv
import json

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/extract/<reference>', methods=['GET'])
@cross_origin(methods=['GET'])
def get_palette(reference):

    reference = "fix-me-palettes/%s.json" % reference

    if not os.path.exists(palette):
        flask.abort(404)

    sb = cooperhewitt.swatchbook.palette(reference)

    path = flask.request.args.get('path')

    if not path:
        flask.abort(400)

    if not os.path.exists(path):
        flask.abort(404)

    # Validate path here

    roy = roygbiv.Roygbiv(path)
    average = roy.get_average_hex()
    palette = roy.get_palette_hex()

    def prep(hex):
        c_hex, c_name = sb.closest_colour(hex)        
        return {'color': c_hex, 'closest': closest}

    average = prep(average)
    palette = map(prep, palette)
    
    rsp = {
        'reference-closest': reference,
        'average': average, 'palette': palette
    }

    return flask.jsonify(**rsp)

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)

#!/usr/bin/env python

import os
import os.path

import flask
from flask_cors import cross_origin 

import cooperhewitt.swatchbook
import roygbiv

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

def build_path(path=None):

    # TO DO: read from config / env
    root = None

    if not root or not os.path.isdir(root):
        logging.error("Missing root")
        flask.abort(500)

    if not path:
        logging.error("Missing path")
        flask.abort(400)

    path = flask.safe_join(root, path)

    if not path:
        logging.error("path considered harmful")
        flask.abort(400)

    path = os.path.join(root, path)
    return path

def ensure_path(path=None):

    path = build_path(path)

    if not os.path.exists(path):
        logging.error("'%s' does not exist" % path)
        flask.abort(404)

    return path

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():
    rsp = {'stat': 'ok'}
    return flask.jsonify(**rsp)

@app.route('/extract/<reference>', methods=['GET'])
@cross_origin(methods=['GET'])
def get_palette(reference):

    logging.debug("get palette with %s" % reference)

    try:
        ref = cooperhewitt.swatchbook.load_palette(reference)
    except Exception, e:
        logging.error(e)
        flask.abort(404)

    path = flask.request.args.get('path')

    if not path:
        flask.abort(400)

    path = ensure_path(path)

    # Validate path here

    roy = roygbiv.Roygbiv(path)
    average = roy.get_average_hex()
    palette = roy.get_palette_hex()

    def prep(hex):
        c_hex, c_name = ref.closest(hex)        
        return {'color': hex, 'closest': c_hex}

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

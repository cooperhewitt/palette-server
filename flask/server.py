#!/usr/bin/env python

import os
import os.path

import flask
from flask_cors import cross_origin 
from werkzeug.contrib.fixers import ProxyFix

import cooperhewitt.swatchbook
import roygbiv

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

def build_path(path=None):

    root = os.environ.get('PALETTE_SERVER_IMAGE_ROOT', None)

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

@app.route('/extract', methods=['GET'])
@cross_origin(methods=['GET'])
def extract_roy():
    return extract_roygbiv('css3')

@app.route('/extract/roygbiv', methods=['GET'])
@cross_origin(methods=['GET'])
def extract_roy_explicit():
    return extract_roygbiv('css3')

@app.route('/extract/roygbiv/<reference>', methods=['GET'])
@cross_origin(methods=['GET'])
def extract_roygbiv(reference):

    path = flask.request.args.get('path')

    if not path:
        logging.error('Missing path')
        flask.abort(400)

    path = ensure_path(path)

    try:
        ref = cooperhewitt.swatchbook.load_palette(reference)
    except Exception, e:
        logging.error(e)
        flask.abort(404)

    logging.debug("get palette for %s, with %s" % (path, reference))

    try:
        roy = roygbiv.Roygbiv(path)
        average = roy.get_average_hex()
        palette = roy.get_palette_hex()

    except Exception, e:
        logging.error(e)
        flask.abort(500)

    def prep(hex):
        c_hex, c_name = ref.closest(hex)        
        return {'color': hex, 'closest': c_hex}

    try:
        average = prep(average)
        palette = map(prep, palette)
    except Exception, e:
        logging.error(e)
        flask.abort(500)
        
    rsp = {
        'reference-closest': reference,
        'average': average,
        'palette': palette
    }

    return flask.jsonify(**rsp)

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)

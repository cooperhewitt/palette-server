#!/usr/bin/env python

import roygbiv
import webcolors
import json
import cgi
import Image
import logging
logging.basicConfig(level=logging.DEBUG)

def app(environ, start_response):

    # https://bitbucket.org/ubernostrum/webcolors/src/b93975d4507fbf0a500656cb475dbd8ddae7a549/webcolors.py?at=default#cl-191

    def closest_colour(requested_colour):
        min_colours = {}

        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_closest(hex):

        rgb = webcolors.hex_to_rgb(hex)

        try:
            closest_name = actual_name = webcolors.rgb_to_name(rgb)
        except ValueError:
            closest_name = closest_colour(rgb)
            actual_name = None

        if actual_name:
            actual = webcolors.name_to_hex(actual_name)
        else:
            actual = None

        closest = webcolors.name_to_hex(closest_name)

        return actual, closest

    def prep(hex):

        web_actual, web_closest = get_closest(hex)

        return {
            'colour': hex,
            'closest': web_closest,
            }

    def get_palette(path):

        roy = roygbiv.Roygbiv(path)
        average = roy.get_average_hex()
        palette = roy.get_palette_hex()

        average = prep(average)
        palette = map(prep, palette)

        return { 'reference-closest': 'css3', 'average': average, 'palette': palette }
    
    status = '200 OK'
    rsp = {}

    params = cgi.parse_qs(environ.get('QUERY_STRING', ''))

    path = params.get('path', None)

    if not path:
        if 'favicon.ico' in environ.get('PATH_INFO', ''):
            rsp = {'stat': 'ok', 'error': 'shh'}
        else:
            rsp = {'stat': 'error', 'error': 'missing image'}
        return iter([rsp])

    else:

        path = path[0]

        try:
            rsp = get_palette(path)
            rsp['stat']  = 'ok'
        except Exception, e:
            logging.error(e)
            rsp = {'stat': 'error', 'error': "failed to process image: %s" % e}
    
    if rsp['stat'] != 'ok':
        status = "500 SERVER ERROR"

    if params.get('debug', None) != None:
        html = '<h1>palette-server debug</h1>'
        with open(path, "rb") as f:
            data = f.read()
            html += '<img width="500px" src="data:;base64,{0}" /><br/>'.format(data.encode("base64"))
        for c in rsp['palette']:
            html += '<span style="display:inline-block;width:25px;height:25px;margin:10px;background-color:{0};">&nbsp;</span>'.format(c['colour'])
        rsp = html
        start_response(status, [
                ('Content-Type', 'text/html'),
                ("Content-Length", str(len(rsp)))
                ])
    else:
        rsp = json.dumps(rsp)
        logging.debug("%s : %s" % (path, status))

        start_response(status, [
                ("Content-Type", "text/javascript"),
                ("Content-Length", str(len(rsp)))
                ])

    return iter([rsp])


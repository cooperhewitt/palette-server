import roygbiv
import json
import cgi

def app(environ, start_response):

    def get_palette(path):
        roy = roygbiv.Roygbiv(path)
        average = roy.get_average_hex()
        palette = roy.get_palette_hex()

        return { 'average': average, 'palette': palette }

    status = '200 OK'
    rsp = {}

    params = cgi.parse_qs(environ.get('QUERY_STRING', ''))

    path = params.get('path', None)

    if not path:
        rsp = {'stat': 'error', 'error': 'missing image'}

    else:

        path = path[0]

        try:
            rsp = get_palette(path)
            rsp['stat']  = 'ok'
        except Exception, e:
            rsp = {'stat': 'error', 'error': "failed to process image: %s" % e}
        
    if rsp['stat'] != 'ok':
        status = "500 SERVER ERROR"

    rsp = json.dumps(rsp)

    start_response(status, [
            ("Content-Type", "text/javascript"),
            ("Content-Length", str(len(rsp)))
            ])

    return iter([rsp])


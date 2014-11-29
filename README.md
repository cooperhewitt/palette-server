# palette-server

palette-server is a small Flask based HTTP-pony to extract colours from an image.

**This package is officially DEPRECATED. You should consult [plumbing-palette-server](https://github.com/cooperhewitt/plumbing-palette-server) instead.**

## How to use it

	$> curl  'http://localhost:5000/extract?path=cat.jpg' | python -m json.tool

	{
		"reference-closest": "css3",
		"average": {
			"closest": "#808080", 
			"colour": "#8e895a", 
		}, 
		"palette": [
			{
				"closest": "#a0522d", 
				"colour": "#957d34", 
		        }, 
        		{
				"closest": "#556b2f", 
				"colour": "#786438", 
		        }, 
		        {
				"closest": "#bdb76b", 
				"colour": "#b0a370", 
		        }, 
		        {
				"closest": "#556b2f", 
				"colour": "#576710", 
		        }, 
		        {
				"closest": "#808080", 
				"colour": "#827968", 
		        }
		], 
		"stat": "ok"
	}

Did you notice the way the path for the request is `/extract`? There are two reasons for that:

* Backwards compatibility with earlier versions of `palette-server`
* Syntactic sugar to hide the colour analysis tool and the colour reference that we're using (to determine the "closest" colour).

Currently there is only one colour analysis tool – Giv Parvaneh's [RoyGBiv](https://github.com/givp/RoyGBiv) – but there may be others some day. You can address it directly like this:

	$> curl  'http://localhost:5000/extract/roygbiv/?path=cat.jpg'

`palette-server` also allows you to pair the colour palette to any reference grid that the [cooperhewitt-swatchbook](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook) library exports. For example, if you want to use the Crayola crayon colour scheme as a reference you could say:

	$> curl  'http://localhost:5000/extract/roygbiv/crayola?path=cat.jpg'

The default reference grid is CSS3.

If you just want to test that the server is up and running you can call the `/ping` endpoint, like this:

	$> curl  'http://localhost:5000/ping'

	{
		"stat": "ok"
	}

## How to run it

### First things first

#### Images

`palette-server` limits itself to processing only those images that it can find in a user-defined directory. Currently this is being configued as an environment variable (mostly because none of the configuration options for Flask stand out as "simple"). For example:

	$> EXPORT PALETTE_SERVER_IMAGE_ROOT=/path/to/images

_Alternative suggestions and patches are welcome. This works but is not awesome, by any means._

#### Authentication and authorization

There is none, by default. This is not necessarily a service that is meant to be public-facing and assumes that unless you are planning to open things up to the world that you are running on a machine with suitable access control restrictions at the network layer.

### Flask

`palette-server` is a Flask application so you can start it up, from the command-line, like this:

	$> cd palette-server
	$> EXPORT PALETTE_SERVER_IMAGE_ROOT=/path/to/images
	$> python flask/server.py

	INFO:werkzeug: * Running on http://127.0.0.1:5000/
	INFO:werkzeug: * Restarting with reloader

### gunicorn

`palette-server` will work with any WSGI-compliant server architecture but there are [sample configuration files and `init.d` scripts](https://github.com/cooperhewitt/palette-server/tree/master/init.d) included with this repository for running things, as a daemonized service, under [gunicorn](http://www.gunicorn.org).

# To do

* HTTP `POST` support (upload files)
* Get from URL support
* Better config options
* A build-pack for Heroku, and friends
* A proper setup file or build script for dependencies

# Dependencies

* [cooperhewitt-swatchbook](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook)
* [numpy](http://pypi.python.org/pypi/numpy)
* [webcolors](http://pypi.python.org/pypi/webcolors/)
* [colormath](http://pypi.python.org/pypi/colormath/)
* [RoyGBiv](https://github.com/givp/RoyGBiv)
* [Flask](http://flask.pocoo.org/)

# See also

* [All your color are belong to Giv](http://labs.cooperhewitt.org/2013/giv-do/)	
* [Using python and k-means to find the dominant colors in images](http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/)
* [colorific](https://github.com/99designs/colorific)

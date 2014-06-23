# palette-server

palette-server is a small Flask based HTTP-pony to extract colours from an image.

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

See how the path is `/extract`. That's just a little bit of syntactic sugar to hide the colour analysis tool that we're using. Currently there is only one, Giv Parvaneh's [RoyGBiv](https://github.com/givp/RoyGBiv) but there may be others some day. You can address it directly like this:

	$> curl  'http://localhost:5000/extract/roygbiv/?path=cat.jpg'

... that the [cooperhewitt-swatchbook]() library exports. For example, if you want to use the Crayola crayon colour grid as a reference you could say:

	$> curl  'http://localhost:5000/extract/roygbiv/crayola?path=cat.jpg'

## How to run it

### Flask

	$> cd palette-server
	$> EXPORT PALETTE_SERVER_IMAGE_ROOT=/path/to/images
	$> python flask/server.py

### gunicorn

TBW

# To do

* HTTP `POST` support
* Get from URL support
* Better config options

# Dependencies

* [cooperhewitt-swatchbook]()
* [numpy](http://pypi.python.org/pypi/numpy)
* [webcolors](http://pypi.python.org/pypi/webcolors/)
* [colormath](http://pypi.python.org/pypi/colormath/)
* [RoyGBiv](https://github.com/givp/RoyGBiv)
* [Flask]()

# See also

* [All your color are belong to Giv](http://labs.cooperhewitt.org/2013/giv-do/)	
* [Using python and k-means to find the dominant colors in images](http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/)
* [colorific](https://github.com/99designs/colorific)

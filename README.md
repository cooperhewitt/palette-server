# palette-server

palette-server is a small littel Flask based HTTP-pony to extract colours from an image.

## How to run it

### Simple

	$> cd palette-server
	$> EXPORT PALETTE_SERVER_IMAGE_ROOT=/path/to/images
	$> python flask/server.py

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

### More complicated (gunicorn)

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

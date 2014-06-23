palette-server
==

palette-server is a small little WSGI-compliant httpony to extract colours from an image.

How to run it
--

I don't know yet. In the meantime:

	$> cd palette-server/bin
	$> gunicorn palette-server:app

There's also a stub `init.d` script in the `init.d` directory. You will need to
adjust the specifics (paths, gunicorn configs. etc.) to taste. Either way you
get the palette server to tell you things by invoking it like this:

	$>curl  'http://localhost:8000?path=/Users/asc/Desktop/cat.jpg' | python -m json.tool

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

To do
--

* Unbundle all the private/locally scoped functions inside of the `app` function. It works but it's kind of stupid.

* Import the [colour-utils colour.py
  code](https://github.com/straup/colour-utils/blob/master/python/colour.py) and
  allow for custom palettes when calculating the closest colour(s) for a
  palette. Currently the server is hard-coded to "snap to grid" using the CSS3
  palette.

* Add the ability to pass a URL (which will mean patching the RoyGBiv
constructor to accept a PIL.Image object rather than a filename) ... maybe

* A proper `setup.py` script for installing dependencies (see below).

* A proper `init.d` script (or equivalent) for starting and stopping the
  palette-server.

Dependencies
--

* [numpy](http://pypi.python.org/pypi/numpy)

* [webcolors](http://pypi.python.org/pypi/webcolors/)

* [colormath](http://pypi.python.org/pypi/colormath/)

* [RoyGBiv](https://github.com/givp/RoyGBiv)

* [gunicorn](http://www.gunicorn.org/)

See also
--

* [All your color are belong to Giv](http://labs.cooperhewitt.org/2013/giv-do/)	
* [Using python and k-means to find the dominant colors in images](http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/)
* [colorific](https://github.com/99designs/colorific)

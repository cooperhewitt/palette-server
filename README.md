palette-server
==

palette-server is a dumb little (wsgi) httpony to extract colours from an image.

How to run it
--

I don't know yet. In the meantime:

	$> cd palette-server/bin
	$> gunicorn palette-server:app

	$>curl  'http://localhost:8000?path=/Users/asc/Desktop/cat.jpg' | python -m json.tool

	{
	    "average": "#8e895a", 
	    "palette": [
	        "#957d34", 
	        "#786438", 
	        "#b0a370", 
	        "#576710", 
	        "#827968"
	    ], 
	    "stat": "ok"
	}

To do
--

* Add the ability to pass a URL (which will mean patching the RoyGBiv
constructor to accept a PIL.Image object rather than a filename) ... maybe

Dependencies
--

* [numpy](http://pypi.python.org/pypi/numpy)

* [webcolors](http://pypi.python.org/pypi/webcolors/)

* [colormath](http://pypi.python.org/pypi/colormath/)

* [gunicorn](http://www.gunicorn.org/)

See also
--

* [RoyGBiv](https://github.com/givp/RoyGBiv)

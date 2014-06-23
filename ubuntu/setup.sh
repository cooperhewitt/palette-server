#!/bin/sh

apt-get install python-numpy python-setuptools python-imaging
easy_install webcolors colormath RoyGBiv

# Strictly speaking these aren't necessary but I like them

sudo apt-get install python-gevent

# Ensure we get gunicorn 18.x or higher

easy_install --upgrade gunicorn

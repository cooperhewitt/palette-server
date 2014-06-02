#!/bin/sh

apt-get install python-numpy python-setuptools python-imaging
easy_install webcolors colormath RoyGBiv

sudo easy_install flask
sudo easy_install flask-cors

sudo apt-get install python-gevent
sudo easy_install --upgrade gunicorn

# Running palette-server using gunicorn and init.d

_This assumes a Unix/Linux system. The following instructions do not apply for OS X or Windows._

First create local copies of the sample config file (for gunicorn) and shell scripts (for init.d)

	$> cd init.d      
	$> cp palette-server.cfg.example palette-server.cfg
	$> cp palette-server.sh.example palette-server.sh

## palette-server.cfg
 
You will need to update `palette-server.cfg` with the relevant paths and other configurations specific to your setup. This is what the sample config file looks like:

	# http://gunicorn-docs.readthedocs.org/en/latest/configure.html#configuration-file

	import os
	import multiprocessing

	workers = multiprocessing.cpu_count() * 2 + 1
	worker_class = "egg:gunicorn#gevent"

	# These are things you might need to change, in particular `images` and `chdir`
	# which are where to look for images and where to look for the server code (to
	# be run by gunicorn) respectively.

	bind = '127.0.0.1:8228'
	chdir = '/usr/local/palette-server/flask'
	user = 'www-data'
	images = '/where/to/look/for/images'

	os.environ['PALETTE_SERVER_IMAGE_ROOT'] = images

## palette-server.sh

You will need to update `palette-server.sh` to point to the correct path for your config file that you've just edited. The relevant bit is:

	PALETTE_SERVER_CONFIG='/usr/local/palette-server/init.d/palette-server.cfg'

## init.d

Link your init.d shell script in to `/etc/init.d` and tell the operating system to make sure it runs when the machine starts up:

	$> sudo ln -s /usr/local/palette-server/init.d/palette-server.sh /etc/init.d/palette-server.sh
	$> sudo update-rc.d palette-server.sh defaults

You can run the server in debug-mode like:

	$> sudo /etc/init.d/palette-server.sh debug

Otherwise all the usual `/etc/init.d` conventions apply:

	$> sudo /etc/init.d/palette-server.sh start
	$> sudo /etc/init.d/palette-server.sh stop

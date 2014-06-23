# init.d

## palette-server.cfg

	$> cp palette-server.cfg.example palette-server.cfg

You will need to update `palette-server.cfg` with the relevant paths and other configurations specific to your setup.

## palette-server.sh

	$> cp palette-server.sh.example palette-server.sh

You will need to update `palette-server.sh` to point to the correct path for your config file.

## init.d

	$> sudo ln -s /usr/local/palette-server/init.d/palette-server.sh /etc/init.d/palette-server.sh
	$> sudo update-rc.d palette-server.sh defaults
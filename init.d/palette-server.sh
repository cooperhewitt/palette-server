#!/bin/sh -e

# Starts, stops, and restarts the event server
# http://werxltd.com/wp/2012/01/05/simple-init-d-script-template/

# To make sure this runs at startup, do:
# update-rc.d palette-server.sh defaults

# Adjust to taste
PS_ROOT='/usr/local/cooperhewitt/palette-server/bin/'

GUNICORN=`which gunicorn`
GUNICORN_OPTS=''

PIDFILE=/var/run/palette-server.pid

case $1 in
    start)
        echo "Starting event server"

	cd $PS_ROOT
	PID=`exec sudo -u www-data $GUNICORN $GUNICORN_OPTS palette-server:app > /dev/null 2>&1 & echo $!`

        if [ -z $PID ]; then
            printf "%s\n" "Fail"
        else
            echo $PID > $PIDFILE
            printf "%s\n" "Ok"
	    echo $PID
        fi

        ;;
    stop)
        echo "Stopping event server"

	printf "%-50s" "Stopping $NAME"
            PID=`cat $PIDFILE`
            cd $DAEMON_PATH
        if [ -f $PIDFILE ]; then
            kill -HUP $PID
            printf "%s\n" "Ok"
            rm -f $PIDFILE
        else
            printf "%s\n" "pidfile not found"
        fi

        ;;
    restart)
        $0 stop
        $0 start
        ;;
    status)
        printf "%-50s" "Checking event-server..."
        if [ -f $PIDFILE ]; then
            PID=`cat $PIDFILE`
            if [ -z "`ps axf | grep ${PID} | grep -v grep`" ]; then
                printf "%s\n" "Process dead but pidfile exists"
            else
                echo "Running"
            fi
        else
            printf "%s\n" "Service not running"
        fi
	;;
    *)
        echo "Usage: $0 {start|stop|restart|status}" >&2
        exit 1
        ;;
esac

#!/bin/bash

set -e

# import faketpl function
. faketpl

# a trick to get arrays from the host's environment
declare -A BACKEND
eval BACKEND=$BACKEND

(faketpl < /usr/local/etc/haproxy/haproxy.cfg.ftpl > /usr/local/etc/haproxy/haproxy.cfg)

# the rest was taken from the original entrypoint

# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- haproxy "$@"
fi

if [ "$1" = 'haproxy' ]; then
	# if the user wants "haproxy", let's use "haproxy-systemd-wrapper" instead so we can have proper reloadability implemented by upstream
	shift # "haproxy"
	set -- "$(which haproxy-systemd-wrapper)" -p /run/haproxy.pid "$@"
fi

exec "$@"

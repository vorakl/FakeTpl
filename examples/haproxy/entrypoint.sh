#!/bin/bash

set -e

# import faketpl function
. faketpl

# It takes scalar from environment and makes array from it
if [[ -n "${BACKEND}" ]]; then
    declare -A BACKENDS
    eval BACKENDS=${BACKEND};
fi

faketpl < /usr/local/etc/haproxy/haproxy.cfg.ftpl > /usr/local/etc/haproxy/haproxy.cfg

# the rest is taken from the original entrypoint

# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- haproxy "$@"
fi

if [ "$1" = 'haproxy' ]; then
    # if the user wants "haproxy", let's use "haproxy-systemd-wrapper" instead
    # so we can have proper reloadability implemented by upstream
    shift # "haproxy"
    set -- "$(which haproxy-systemd-wrapper)" -p /run/haproxy.pid "$@"
fi

exec "$@"

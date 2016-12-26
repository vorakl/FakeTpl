#!/bin/sh

source faketpl.sh
faketpl < /usr/share/nginx/html/index.html.ftpl > /usr/share/nginx/html/index.html

exec "$@"

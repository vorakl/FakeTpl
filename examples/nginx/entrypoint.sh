#!/bin/sh

source faketpl
(faketpl < /usr/share/nginx/html/index.html.ftpl > /usr/share/nginx/html/index.html)

exec "$@"

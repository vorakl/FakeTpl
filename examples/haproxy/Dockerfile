FROM docker.io/haproxy:1.7-alpine

# we need Bash for arrays
RUN apk add --no-cache bash

RUN wget -qP /usr/bin/ http://faketpl.vorakl.name/faketpl.sh

COPY haproxy.cfg.ftpl /usr/local/etc/haproxy/
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

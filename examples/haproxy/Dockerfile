FROM docker.io/haproxy:1.7-alpine

# we need Bash for arrays
RUN apk add --no-cache bash

RUN wget -qO /usr/bin/faketpl http://faketpl.vorakl.name/faketpl && \
    ( cd /usr/bin && wget -qO - http://faketpl.vorakl.name/faketpl.sha256 | sha256sum -c )  

COPY haproxy.cfg.ftpl /usr/local/etc/haproxy/
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

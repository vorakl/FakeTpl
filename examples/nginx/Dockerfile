FROM nginx:mainline-alpine

COPY entrypoint.sh /
COPY index.html.ftpl /usr/share/nginx/html/

RUN wget -qO /usr/bin/faketpl http://faketpl.vorakl.name/faketpl && \
    ( cd /usr/bin && wget -qO - http://faketpl.vorakl.name/faketpl.sha256 | sha256sum -c )

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

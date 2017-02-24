FROM nginx:mainline-alpine

COPY entrypoint.sh /
COPY index.html.ftpl /usr/share/nginx/html/

RUN wget -qP /usr/bin/ http://vorakl.github.io/FakeTpl/faketpl

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:mainline-alpine

COPY entrypoint.sh /
COPY index.html.ftpl /usr/share/nginx/html/

RUN wget -qP /usr/bin/ http://faketpl.vorakl.name/faketpl.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:alpine as env

FROM env as dev
COPY nginx.dev.conf /etc/nginx/templates/default.conf.template

FROM 'openresty/openresty:alpine-aarch64'

EXPOSE 80
EXPOSE 443

RUN mkdir -p /usr/local/openresty/nginx/conf/vhost \
    && mkdir -p /usr/local/openresty/nginx/conf/extra \
    && mkdir -p /usr/local/openresty/nginx/conf/certs \
    && mkdir -p /usr/local/openresty/nginx/conf/tcp_proxy \
    && mkdir -p /usr/local/openresty/nginx/html

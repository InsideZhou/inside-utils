FROM 'openresty/openresty:focal'

ENV LANG="zh_CN.UTF-8" \
	LANGUAGE="zh_CN:zh:en_US:en" \
	LC_MESSAGES="en_US.UTF-8" \
	TIMEZONE="Asia/Shanghai"

RUN apt-get update

RUN printf "en_US.UTF-8 UTF-8 \nzh_CN.UTF-8 UTF-8" > /etc/locale.gen
RUN apt-get -y install locales tzdata
RUN locale-gen && \
	echo $TIMEZONE > /etc/timezone && \
	rm /etc/localtime && \
	ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
	dpkg-reconfigure -f noninteractive tzdata

RUN apt-get clean

RUN mkdir -p /usr/local/openresty/nginx/conf/vhost \
    && mkdir -p /usr/local/openresty/nginx/conf/extra \
    && mkdir -p /usr/local/openresty/nginx/conf/certs \
    && mkdir -p /usr/local/openresty/nginx/conf/tcp_proxy \
    && mkdir -p /usr/local/openresty/nginx/html

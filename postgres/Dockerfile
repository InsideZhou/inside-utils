FROM 'postgres:14'

ENV TIMEZONE="Asia/Shanghai"

COPY timescale-timescaledb-E7391C94080429FF.pub.gpg /root/
RUN cat /root/timescale-timescaledb-E7391C94080429FF.pub.gpg | gpg --dearmor --output /usr/share/keyrings/timescaledb.keyring
RUN echo "deb [signed-by=/usr/share/keyrings/timescaledb.keyring] https://packagecloud.io/timescale/timescaledb/debian/ bullseye main" > /etc/apt/sources.list.d/timescaledb.list

RUN apt-get update

RUN printf "en_US.UTF-8 UTF-8 \nzh_CN.UTF-8 UTF-8" > /etc/locale.gen
RUN apt-get -y install locales tzdata
RUN locale-gen && \
	echo $TIMEZONE > /etc/timezone && \
	rm /etc/localtime && \
	ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
	dpkg-reconfigure -f noninteractive tzdata && \
	localedef -i zh_CN -c -f UTF-8 -A /usr/share/locale/locale.alias zh_CN.UTF-8

ENV LANG="zh_CN.UTF-8" \
	LC_MESSAGE="en_US.UTF-8"

RUN apt-get -y install vim git
RUN apt-get clean

RUN printf "set shiftwidth=4\nset tabstop=4\nset softtabstop=4\nset autoindent\nset smartindent " >> /etc/vim/vimrc.local
RUN printf "alias ll='ls -Alh'\n" >> /etc/bash.bashrc

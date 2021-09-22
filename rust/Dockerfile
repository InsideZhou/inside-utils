FROM 'rust'

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

RUN apt-get -y install vim git
RUN apt-get clean

RUN printf "set shiftwidth=4\nset tabstop=4\nset softtabstop=4\nset autoindent\nset smartindent " >> /etc/vim/vimrc.local
RUN printf "alias ll='ls -AlH'\n" >> /etc/bash.bashrc

COPY ./config /root/.cargo/
RUN cargo search --limit 0

FROM 'azul/zulu-openjdk:11'

ENV LANG="zh_CN.UTF-8" \
    LANGUAGE="zh_CN:zh:en_US:en" \
    LC_MESSAGES="en_US.UTF-8" \
    TIMEZONE="Asia/Shanghai"

COPY locale.gen /etc/locale.gen
RUN locale-gen \
    && echo $TIMEZONE > /etc/timezone \
    && apt-get update && apt-get install -y tzdata \
    && rm /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean
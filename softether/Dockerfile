FROM ubuntu:focal

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install cmake gcc g++ make libncurses5-dev libssl-dev libsodium-dev libreadline-dev zlib1g-dev

COPY ./ /opt/SoftEtherVPN
WORKDIR /opt/SoftEtherVPN
RUN chmod a+x configure
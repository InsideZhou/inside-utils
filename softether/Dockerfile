FROM ubuntu:focal

RUN apt-get update
RUN apt-get -y install cmake gcc g++ make libncurses5-dev libssl-dev libsodium-dev libreadline-dev zlib1g-dev

COPY ./ /opt/SoftEtherVPN
WORKDIR /opt/SoftEtherVPN
RUN chmod a+x configure
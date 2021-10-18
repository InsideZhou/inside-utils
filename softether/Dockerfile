FROM ubuntu:focal

RUN apt-get update
RUN apt-get -y install cmake gcc g++ make libncurses5-dev libssl-dev libsodium-dev libreadline-dev zlib1g-dev
RUN apt-get clean

COPY ./ /opt/SoftEtherVPN
WORKDIR /opt/SoftEtherVPN

RUN chmod a+x configure
RUN make -C build
RUN make -C build install
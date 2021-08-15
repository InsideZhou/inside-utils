FROM centos:7

RUN groupadd kingbase && useradd -g kingbase -m -d /opt/kingbase -s /bin/bash kingbase

WORKDIR /opt/kingbase

ADD kingbase.tar.gz ./

ADD docker-entrypoint.sh ./

ADD license.dat ./Server/bin/

ADD kingbase.conf ./

RUN mkdir -p data

RUN chmod +x docker-entrypoint.sh

RUN chown -R kingbase:kingbase /opt/kingbase

ENV PATH /opt/kingbase/Server/bin:$PATH

ENV DB_VERSION V008R003C002B0320

USER kingbase

EXPOSE 54321

ENTRYPOINT ["/opt/kingbase/docker-entrypoint.sh"]
FROM ubuntu:jammy as app

ARG PLASMIDFINDER_VER="2.1.6"
ARG PLASMIDFINDER_DB_DATE="2023-03-17"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="plasmidfinder"
LABEL software.version="${PLASMIDFINDER_VER}"
LABEL description="Identifies plasmids in total or partial sequenced isolates of bacteria."
LABEL website="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/README.md"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3-biopython \
    python3-cgecore \
    python3-tabulate \
    python3-distutils \
    kma \
    ncbi-blast+ &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://bitbucket.org/genomicepidemiology/plasmidfinder/get/${PLASMIDFINDER_VER}.tar.gz && \
    tar -C /usr/local/bin/ --strip-components=1 --wildcards -xvf ${PLASMIDFINDER_VER}.tar.gz */plasmidfinder.py &&\
    rm ${PLASMIDFINDER_VER}.tar.gz &&\
    wget --no-check-certificate https://bitbucket.org/genomicepidemiology/plasmidfinder_db/get/314d85f43e4e018baf35a2b093d9adc1246bc88d.tar.gz &&\
    mkdir plasmidfinder_db &&\
    tar -C /plasmidfinder_db --strip-components=1 -xvf 314d85f43e4e018baf35a2b093d9adc1246bc88d.tar.gz &&\
    rm 314d85f43e4e018baf35a2b093d9adc1246bc88d.tar.gz &&\
    cd plasmidfinder_db && python3 INSTALL.py kma_index &&\
    echo ${PLASMIDFINDER_DB_DATE} > DB_DATE

ENV LC_ALL=C

WORKDIR /data
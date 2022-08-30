FROM ubuntu:focal as app

ARG SOFTWARENAME_VER="5.4.3"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Unofficial Lite version of BUSCO"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    python3-pip \
    prodigal \
    hmmer \
    openjdk-8-jre-headless \
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install bbtools
RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_38.98.tar.gz &&\
    tar -xvf BBMap_38.98.tar.gz &&\
    rm BBMap_38.98.tar.gz &&\
    mv /bbmap/* /usr/local/bin/

# Install BUSCO
RUN python3 -m pip install --no-cache-dir -U pandas biopython==1.73 &&\
    wget https://gitlab.com/ezlab/busco/-/archive/5.4.3/busco-5.4.3.tar.gz &&\
    tar -xvf busco-5.4.3.tar.gz && \
    rm busco-5.4.3.tar.gz &&\
    cd busco-5.4.3 && \
    python3 setup.py install

WORKDIR /data
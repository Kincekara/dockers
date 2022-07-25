FROM ubuntu:focal as app

ARG SOFTWARENAME_VER="5.3.2"

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
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Instal BUSCO
RUN python3 -m pip install --no-cache-dir -U pandas biopython==1.73 &&\
    wget https://gitlab.com/ezlab/busco/-/archive/5.3.2/busco-5.3.2.tar.gz &&\
    tar -xvf busco-5.3.2.tar.gz && \
    rm busco-5.3.2.tar.gz &&\
    cd busco-5.3.2 && \
    python3 setup.py install

WORKDIR /data

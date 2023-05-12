FROM ubuntu:focal

ARG SOFTWARENAME_VER="2.3"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="MASH"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install -y wget pigz &&\
    rm -rf /var/lib/apt/lists/* && apt-get autoclean &&\
    wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar &&\
    tar -xvf mash-Linux64-v2.3.tar --no-same-owner &&\
    rm mash-Linux64-v2.3.tar 

ENV PATH="${PATH}:/mash-Linux64-v2.3/"

WORKDIR /data
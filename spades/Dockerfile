FROM ubuntu:focal

ARG SOFTWARENAME_VER="3.15.5"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SPAdes"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="SPAdes - St. Petersburg genome assembler"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install -y \
    wget \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget http://cab.spbu.ru/files/release3.15.5/SPAdes-3.15.5-Linux.tar.gz &&\
    tar -xzf SPAdes-3.15.5-Linux.tar.gz &&\
    rm SPAdes-3.15.5-Linux.tar.gz

ENV PATH="${PATH}:/SPAdes-3.15.5-Linux/bin/"

WORKDIR /data
FROM alpine:3.12

ARG SOFTWARENAME_VER="2.7"

LABEL base.image="alpine:3.12"
LABEL dockerfile.version="1"
LABEL software="Bracken"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Bayesian Reestimation of Abundance with Kraken"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk update && apk add --no-cache wget bash python3 tar &&\
    ln -s /usr/bin/python3 /usr/bin/python &&\
    wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/v2.7.tar.gz &&\
    tar -xvf v2.7.tar.gz

ENV PATH="${PATH}:/Bracken-2.7"

WORKDIR /data
FROM alpine:3.12

ARG SOFTWARENAME_VER="0.23.2"

LABEL base.image="alpine:3.12"
LABEL dockerfile.version="1"
LABEL software="FASTP"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="FASTP and JQ"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache wget jq bash &&\
    wget http://opengene.org/fastp/fastp.0.23.2 &&\
    mv fastp.0.23.2 /usr/bin/fastp &&\
    chmod a+x /usr/bin/fastp

WORKDIR /data
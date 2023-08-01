FROM alpine:3.18

ARG FASTP_VER="0.23.4"

LABEL base.image="alpine:3.18"
LABEL dockerfile.version="1"
LABEL software="FASTP"
LABEL software.version=$FASTP_VER
LABEL description="FASTP and JQ"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache wget jq bash &&\
    wget http://opengene.org/fastp/fastp.${FASTP_VER} &&\
    mv fastp.${FASTP_VER} /usr/bin/fastp &&\
    chmod a+x /usr/bin/fastp

WORKDIR /data
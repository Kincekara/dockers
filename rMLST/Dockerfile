FROM alpine:3.17.1

ARG SOFTWARENAME_VER="0.1"

LABEL base.image="alpine:3.17.1"
LABEL dockerfile.version="1"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="rMLST Species identification via RESTful API"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache bash curl jq

COPY rmlst.sh /usr/local/bin

WORKDIR /data
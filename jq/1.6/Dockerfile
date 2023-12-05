FROM alpine:3.18

ARG JQ_VER="1.6"

LABEL base.image="alpine:3.18"
LABEL dockerfile.version="1"
LABEL software="JQ"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="command-line JSON processor"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk update && apk add --no-cache \
    bash \
    jq \
    tzdata

ENV LC_ALL=C TZ=US/Eastern

CMD bash

WORKDIR /data
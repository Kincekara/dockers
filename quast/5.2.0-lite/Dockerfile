FROM alpine:3.18

RUN apk update && apk add --no-cache bash py3-pip &&\
    pip install quast==5.2.0

WORKDIR /data
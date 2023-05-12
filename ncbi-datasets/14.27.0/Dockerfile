FROM alpine:3.15

ARG SOFTWARENAME_VER="v14.27.0"

LABEL base.image="alpine:3.15"
LABEL dockerfile.version="1"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="NCBI's datasets and dataformat"
LABEL license="https://github.com/ncbi/datasets/blob/master/pkgs/ncbi-datasets-cli/LICENSE.md"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache bash jq wget pigz tar unzip &&\
wget --no-check-certificate --content-disposition https://github.com/ncbi/datasets/releases/download/${SOFTWARENAME_VER}/linux-amd64.cli.package.zip &&\
unzip linux-amd64.cli.package.zip && rm linux-amd64.cli.package.zip &&\
mv datasets dataformat /usr/local/bin

ENV LC_ALL=C

WORKDIR /data
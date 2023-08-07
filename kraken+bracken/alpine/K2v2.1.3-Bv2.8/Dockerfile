ARG KRAKEN_VER="2.1.3"
ARG BRACKEN_VER="2.8"

## Builder ##
FROM alpine:3.18 AS builder

ARG KRAKEN_VER
ARG BRACKEN_VER

RUN apk update && apk add build-base make bash perl tar zlib-dev

# Install Kraken2
RUN wget  https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN_VER}.tar.gz &&\
    tar -xvf v${KRAKEN_VER}.tar.gz &&\
    cd kraken2-${KRAKEN_VER} &&\
    ./install_kraken2.sh /kraken2
# install Bracken
RUN wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/v${BRACKEN_VER}.tar.gz &&\
    tar -xvf v${BRACKEN_VER}.tar.gz &&\
    cd Bracken-2.8 &&\
    chmod 755 install_bracken.sh && ./install_bracken.sh

## App ##
FROM alpine:3.18 AS app

ARG KRAKEN_VER
ARG BRACKEN_VER

LABEL base.image="alpine:3.18"
LABEL dockerfile.version="1"
LABEL software="Kraken & Bracken"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Kraken2 with Bracken"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk update && apk add --no-cache bash python3 perl libstdc++ libgcc libgomp rsync pigz
    #ln -s /usr/bin/python3 /usr/bin/python 

COPY --from=builder /kraken2 /kraken2
COPY --from=builder /Bracken-${BRACKEN_VER} /Bracken-${BRACKEN_VER}

ENV PATH="${PATH}:/kraken2:/Bracken-${BRACKEN_VER}"

WORKDIR /data
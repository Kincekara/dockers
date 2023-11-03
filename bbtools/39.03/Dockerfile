FROM alpine:3.18

ARG BBTOOLS_VER="39.03"

LABEL base.image="alpine:3.18"
LABEL dockerfile.version="1"
LABEL software="BBTools"
LABEL software.version="${BBTOOLS_VER}"
LABEL description="BBTools is a suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data."
LABEL website="https://jgi.doe.gov/data-and-tools/software-tools/bbtools/"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache bash wget openjdk8-jre &&\
    wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBTOOLS_VER}.tar.gz &&\
    tar -xvf BBMap_${BBTOOLS_VER}.tar.gz && rm BBMap_${BBTOOLS_VER}.tar.gz

ENV PATH="$PATH:/bbmap"

WORKDIR /data
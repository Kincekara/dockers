FROM ubuntu:jammy

ARG MASH_VER="v2.3"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="MASH"
LABEL software.version=${MASH_VER}
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y wget &&\
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget --no-check-certificate https://github.com/marbl/Mash/releases/download/${MASH_VER}/mash-Linux64-${MASH_VER}.tar &&\
    tar -xvf mash-Linux64-${MASH_VER}.tar --no-same-owner &&\
    rm mash-Linux64-${MASH_VER}.tar &&\
    mv /mash-Linux64-${MASH_VER}/mash /usr/local/bin/

ADD https://drive.google.com/host/15dqAEt0qicyVMKYN1h7UZ5xH_sxbyFdV/cbird_s10k_221222.msh /

WORKDIR /data
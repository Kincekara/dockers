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

# download cbird mash sketch from gdrive
RUN wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1OH5UXvNnBWWLMNsKwz3QwGFB2RML8HV_' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1OH5UXvNnBWWLMNsKwz3QwGFB2RML8HV_" -O cbird_s10k_221222.msh &&\
    rm -rf /tmp/cookies.txt

WORKDIR /data


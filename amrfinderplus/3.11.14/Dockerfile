FROM ubuntu:focal as app

ARG AMRFINDER_VER="v3.11.14"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version=$AMRFINDER_VER
LABEL description="NCBI Antimicrobial Resistance Gene Finder"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y curl hmmer ncbi-blast+ ca-certificates &&\
    rm -rf /var/lib/apt/lists/* && apt-get autoclean &&\    
    curl -LJO https://github.com/ncbi/amr/releases/download/amrfinder_${AMRFINDER_VER}/amrfinder_binaries_${AMRFINDER_VER}.tar.gz &&\
    mkdir /amrfinder &&\
    tar -C /amrfinder -xvf amrfinder_binaries_${AMRFINDER_VER}.tar.gz && rm amrfinder_binaries_${AMRFINDER_VER}.tar.gz

ENV PATH="${PATH}:/amrfinder"

WORKDIR /data
FROM ubuntu:focal as app

ARG SOFTWARENAME_VER="3.10.40"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="NCBI Antimicrobial Resistance Gene Finder"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"


RUN apt-get update && apt-get install --no-install-recommends -y curl hmmer ncbi-blast+ ca-certificates &&\
    mkdir /amrfinder && cd amrfinder &&\
    curl -LJO https://github.com/ncbi/amr/releases/download/amrfinder_v3.10.40/amrfinder_binaries_v3.10.40.tar.gz &&\
    tar -xvf amrfinder_binaries_v3.10.40.tar.gz && rm amrfinder_binaries_v3.10.40.tar.gz

ENV PATH="${PATH}:/amrfinder"

WORKDIR /data







    
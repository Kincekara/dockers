FROM ubuntu:focal as app

ARG SOFTWARENAME_VER="3.11.8"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="NCBI Antimicrobial Resistance Gene Finder"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"


RUN apt-get update && apt-get install --no-install-recommends -y curl hmmer libgomp1 ca-certificates &&\
    rm -rf /var/lib/apt/lists/* && apt-get autoclean &&\
    mkdir /amrfinder && cd amrfinder &&\
    curl -LJO https://github.com/ncbi/amr/releases/download/amrfinder_v3.11.8/amrfinder_binaries_v3.11.8.tar.gz &&\
    tar -xvf amrfinder_binaries_v3.11.8.tar.gz && rm amrfinder_binaries_v3.11.8.tar.gz &&\
    cd / && curl -LJO https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz &&\
    tar -xvf ncbi-blast-2.13.0+-x64-linux.tar.gz && rm ncbi-blast-2.13.0+-x64-linux.tar.gz
    
ENV PATH="${PATH}:/amrfinder:/ncbi-blast-2.13.0+/bin/"

WORKDIR /data







    
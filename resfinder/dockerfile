FROM ubuntu:focal

ARG SOFTWARENAME_VER="4.1.11"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="ResFinder"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="ResFinder identifies acquired antimicrobial resistance genes in total or partial sequenced isolates of bacteria."
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    libgomp1 \
    python3-pip \
    libz-dev \ 
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Get blastn executable
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz &&\
    tar -xvf ncbi-blast-2.13.0+-x64-linux.tar.gz && rm ncbi-blast-2.13.0+-x64-linux.tar.gz &&\
    cp ./ncbi-blast-2.13.0+/bin/blastn /usr/local/bin &&\
    rm -r ncbi-blast-2.13.0+

# Install python dependencies
RUN pip3 install -U biopython==1.73 tabulate cgecore gitpython python-dateutil

# Install modified ResFinder
COPY run_resfinder.py /usr/src/run_resfinder.py
ADD cge /usr/src/cge

ENV PATH="${PATH}:/usr/src"

WORKDIR /data
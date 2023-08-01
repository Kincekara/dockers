FROM ubuntu:focal as app

ARG BUSCO_VER="5.4.7"
ARG BBMAP_VER="39.01"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version=$BUSCO_VER
LABEL description="Unofficial Lite version of BUSCO"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    python3-pip \
    prodigal \
    hmmer \
    openjdk-8-jre-headless \
    gcc-x86-64-linux-gnu \
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VER}.tar.gz &&\
    tar -xvf BBMap_${BBMAP_VER}.tar.gz &&\
    rm BBMap_${BBMAP_VER}.tar.gz &&\
    mv /bbmap/* /usr/local/bin/ &&\
    python3 -m pip install --no-cache-dir -U pandas biopython==1.73 &&\
    wget https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz &&\
    tar -xvf busco-${BUSCO_VER}.tar.gz && \
    rm busco-${BUSCO_VER}.tar.gz &&\
    cd busco-${BUSCO_VER} && \
    python3 setup.py install

WORKDIR /data
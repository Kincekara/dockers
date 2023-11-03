FROM ubuntu:jammy as app

ARG BUSCO_VER="5.4.7"
ARG BBMAP_VER="39.03"
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version=$BUSCO_VER
LABEL description="Unofficial Lite version of BUSCO"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3-biopython \
    python3-setuptools \
    python3-pandas \
    prodigal \
    hmmer \
    openjdk-8-jre-headless \
    gcc-x86-64-linux-gnu &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install bbmap & busco
RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VER}.tar.gz &&\
    tar -xvf BBMap_${BBMAP_VER}.tar.gz &&\
    rm BBMap_${BBMAP_VER}.tar.gz &&\
    mv /bbmap/* /usr/local/bin/ &&\
    wget https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz &&\
    tar -xvf busco-${BUSCO_VER}.tar.gz && \
    rm busco-${BUSCO_VER}.tar.gz &&\
    cd busco-${BUSCO_VER} && \
    python3 setup.py install

# download bacteria dataset
RUN busco --download bacteria_odb10

WORKDIR /

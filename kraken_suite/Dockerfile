# builder
FROM ubuntu:focal AS builder

ARG KRAKEN_VER="v2.1.2"
ARG BRACKEN_VER="v2.8"
ARG KTOOLS_VER="v1.2"

RUN apt-get update && apt-get install -y build-essential perl wget

# install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/${KRAKEN_VER}.tar.gz &&\
    tar -xvf ${KRAKEN_VER}.tar.gz &&\
    cd kraken2-2.1.2 &&\
    ./install_kraken2.sh /kraken2
# install Bracken
RUN wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/${BRACKEN_VER}.tar.gz &&\
    tar -xvf ${BRACKEN_VER}.tar.gz &&\
    cd Bracken-2.8 &&\
    chmod 755 install_bracken.sh && ./install_bracken.sh

# install KrakenTools
RUN wget https://github.com/jenniferlu717/KrakenTools/archive/refs/tags/${KTOOLS_VER}.tar.gz &&\
    tar -xvf ${KTOOLS_VER}.tar.gz
    
# App
FROM ubuntu:focal AS app

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Kraken v2.1.2, Bracken v2.8, KrakenTools v1.2"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Kraken2, Bracken and KrakenTools"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install -y perl python-is-python3 python3-biopython libgomp1 pigz \
&& rm -rf /var/lib/apt/lists/* && apt-get autoclean

COPY --from=builder /kraken2 /kraken2
COPY --from=builder /Bracken-2.8 /Bracken-2.8
COPY --from=builder /KrakenTools-1.2 /KrakenTools-1.2

ENV LC_ALL=C
ENV PATH="${PATH}:/kraken2:/Bracken-2.8:/KrakenTools-1.2:/KrakenTools-1.2/DiversityTools/"

WORKDIR /data
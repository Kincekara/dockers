# builder
FROM ubuntu:focal AS builder

RUN apt-get update && apt-get install -y build-essential perl wget

# install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/v2.1.2.tar.gz &&\
    tar -xf v2.1.2.tar.gz &&\
    cd kraken2-2.1.2 &&\
    ./install_kraken2.sh /kraken2
# install Bracken
RUN wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/v2.8.tar.gz &&\
    tar -xvf v2.8.tar.gz && rm v2.8.tar.gz &&\
    cd Bracken-2.8 &&\
    chmod 755 install_bracken.sh && ./install_bracken.sh

# App
FROM ubuntu:focal AS app

ARG KRAKEN_VER="2.1.2"
ARG BRACKEN_VER="2.8"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Kraken & Bracken"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Kraken2 with Bracken"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install -y perl python-is-python3 libgomp1 \
&& rm -rf /var/lib/apt/lists/* && apt-get autoclean

COPY --from=builder /kraken2 /kraken2
COPY --from=builder /Bracken-2.8 /Bracken-2.8

ENV PATH="${PATH}:/kraken2:/Bracken-2.8"


WORKDIR /data
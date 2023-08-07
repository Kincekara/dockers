# builder
FROM ubuntu:focal AS builder

ARG KRAKEN_VER="2.1.3"
ARG BRACKEN_VER="2.8"

RUN apt-get update && apt-get install -y build-essential perl wget zlib1g-dev

# install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN_VER}.tar.gz &&\
    tar -xvf v${KRAKEN_VER}.tar.gz &&\
    cd kraken2-${KRAKEN_VER} &&\
    ./install_kraken2.sh /kraken2
# install Bracken
RUN wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/v${BRACKEN_VER}.tar.gz &&\
    tar -xvf v${BRACKEN_VER}.tar.gz && rm v${BRACKEN_VER}.tar.gz &&\
    cd Bracken-${BRACKEN_VER} &&\
    chmod 755 install_bracken.sh && ./install_bracken.sh

# App
FROM ubuntu:focal AS app

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Kraken & Bracken"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Kraken2 with Bracken"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apt-get update && apt-get install  --no-install-recommends -y perl python-is-python3 libgomp1 pigz \
&& rm -rf /var/lib/apt/lists/* && apt-get autoclean

COPY --from=builder /kraken2 /kraken2
COPY --from=builder /Bracken-2.8 /Bracken

ENV LC_ALL=C
ENV PATH="${PATH}:/kraken2:/Bracken"

WORKDIR /data
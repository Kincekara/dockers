FROM alpine:3.15

ARG CBIRD_UTIL_VER="1.3"
ARG DATASETS_VER="v16.34.1"

LABEL base.image="alpine:3.15"
LABEL dockerfile.version="1"
LABEL software.version=${CBIRD_UTIL_VER}
LABEL description="C-BIRD utility tool"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache bash python3 py3-pandas jq wget py3-lxml py3-argparse py3-numpy &&\
    wget https://github.com/ncbi/datasets/releases/download/${DATASETS_VER}/linux-amd64.cli.package.zip &&\
    unzip linux-amd64.cli.package.zip && rm linux-amd64.cli.package.zip &&\
    mv datasets dataformat /usr/local/bin/

RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/species_genome_size.txt.gz &&\
    gunzip species_genome_size.txt.gz &&\
    date +%Y-%m-%d > sgs_download_date.txt &&\
    mv species_genome_size.txt sgs_download_date.txt /usr/local/lib/

COPY report_gen.py est_coverage.py qc_report.py /usr/local/bin/

ENV LC_ALL=C

WORKDIR /data
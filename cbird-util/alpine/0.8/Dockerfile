FROM alpine:3.15

ARG SOFTWARENAME_VER="0.8"

LABEL base.image="alpine:3.15"
LABEL dockerfile.version="1"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="C_BIRD utility"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"

RUN apk add --no-cache bash python3 py3-pandas jq wget py3-lxml py3-argparse &&\
mkdir data &&\
wget 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets' &&\
chmod +x datasets && mv datasets /data/

COPY report_gen.py report_gen_m.py est_coverage.py qc_report.py /data/

ENV PATH="${PATH}:/data"

WORKDIR /data
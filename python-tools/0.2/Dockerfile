FROM ubuntu:jammy

LABEL base.image="ubuntu:jammy"
LABEL description="python3 with biopython, pandas, plotly, toytree, toyplot, future, requests, Jinja2, matplotlib, and seaborn libraries"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \   
    python3-pip &&\
    pip install --no-cache-dir biopython pandas plotly toytree toyplot future requests Jinja2 matplotlib seaborn

ENV LC_ALL=C 

WORKDIR /data
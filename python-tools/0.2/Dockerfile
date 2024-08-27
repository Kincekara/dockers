FROM ubuntu:jammy

LABEL base.image="ubuntu:jammy"
LABEL description="python3 with biopython, pandas, plotly, toytree, toyplot, future, requests, Jinja2, matplotlib, and seaborn libraries"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \   
    python3-pip &&\
    pip install --no-cache-dir biopython pandas==2.1.4 plotly toytree==3.0.5 toyplot==1.0.3 future requests Jinja2 matplotlib==3.8.2 seaborn==0.13.0

ENV LC_ALL=C 

WORKDIR /data
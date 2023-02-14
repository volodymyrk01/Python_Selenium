FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get install -y \
        curl \
        wget \
        build-essential \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py \
    && pip install pytest selenium pytest-html pytest-xdist\
    && apt-get remove --purge -y \
        curl \
        wget \
        build-essential \
    && apt-get autoremove -y





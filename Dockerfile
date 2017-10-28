FROM ubuntu:xenial
MAINTAINER Gustavo Nascimento "gunasper@gmail.com"
ENV REFRESHED_AT 2017-10-27

#OS dependences
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git python3.5 python3.5-dev python3-pip python3-setuptools make libpq-dev 

RUN git clone https://github.com/gunasper/test_mm.git

WORKDIR test_mm

ARG build
ENV BUILD $build
RUN git checkout master
RUN make deps

EXPOSE 5000
ENTRYPOINT ["/usr/bin/sh", "make run"]

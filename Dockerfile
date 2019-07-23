FROM ubuntu:latest
MAINTAINER lingojuyogesh.kumar@ltts.com
RUN apt-get update && apt-get install -y \
	python3.7 \
	python3-pip 
RUN pip3 install pycodestyle &&\
	pip3 install --upgrade pycodestyle &&\
	pip3 install autopep8
RUN echo "Docker is ready for python & pycodestyle & Autopep8"


FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY ./requirements.txt /RunBlue/requirements.txt

WORKDIR /RunBlue

RUN pip3 install -r requirements.txt

COPY . /RunBlue

ENTRYPOINT FLASK_APP=RunBlue flask run --host 0.0.0.0 --port 8080

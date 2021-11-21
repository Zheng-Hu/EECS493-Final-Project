FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY ./requirements.txt /runblue/requirements.txt

WORKDIR /runblue

RUN pip3 install -r requirements.txt

COPY . /runblue

ENV FLASK_APP=runblue

ENTRYPOINT FLASK_APP=runblue flask run --host 0.0.0.0 --port 8080

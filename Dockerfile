FROM python:3.7-slim-buster as builder

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir ./work
COPY ./work ./work

WORKDIR ./work

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install opencv-python
RUN pip install opencv-contrib-python
RUN pip install flask
RUN apt-get install -y libgl1-mesa-dev

CMD ["python","flask_app.py"]
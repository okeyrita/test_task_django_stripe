FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN pip install Django \
                stripe

RUN mkdir /test_task
WORKDIR /test_task
ADD . /test_tesk
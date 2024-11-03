FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requirement.txt /app/requirement.txt
RUN pip install -r requirement.txt
COPY . /app

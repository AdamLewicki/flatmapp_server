# pull official base image
FROM python:3.8.3-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install drf-writable-nested
RUN pip install -U drf-yasg
RUN pip install mysqlclient
RUN pip install django-mysql
RUN pip install gunicorn

# copy project
COPY . /usr/src/app/
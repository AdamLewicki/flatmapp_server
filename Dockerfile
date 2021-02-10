# pull official base image
FROM python:3.8.3-buster

# copy project
COPY . /usr/src/app/

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install -r req.txt
# copy project
COPY . /usr/src/app/
# pull the official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /django

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1






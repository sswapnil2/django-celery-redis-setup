FROM python:3.6.8-alpine 

RUN mkdir -p /app

WORKDIR /app 

# set environment variables 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies 
RUN pip install --upgrade pip 

RUN pip install pipenv 

COPY ./Pipfile /app/Pipfile 

RUN pipenv install --skip-lock --system --dev 

COPY . /app
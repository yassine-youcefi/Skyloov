# syntax = docker/dockerfile:1.2.1

FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt-get update && apt-get install -y tzdata
RUN apt install libpq-dev nginx -y
# RUN pip install gunicorn

# Set work directory
WORKDIR /code 
COPY requirements.txt /code/
RUN pip install --upgrade pip
# RUN --mount=type=cache,target=/root/.cache \    
RUN    pip install -r requirements.txt 


EXPOSE 8080
COPY . /code/
# CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "config.wsgi"]
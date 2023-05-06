# Overview

## Skyloov
 Code challenge for Skyloov Property Portal

## Technologies i used

I used Python(3) as Primary language .

## Framework

Django, Django Rest Framework ....

## Requirements

- [Docker file](http://192.168.1.146/neo/neo-api/-/blob/dev/Dockerfile)

  > Contain docker global config ...

- [Docker-compose](http://192.168.1.146/neo/neo-api/-/blob/dev/docker-compose.yml)

  > My docker containers configuration ...

- [requirements.txt](http://192.168.1.146/neo/neo-api/-/blob/dev/requirements.txt)

  > All python requirements ...

<br>
<hr>
<br>

### Start-up

> Pleas follow the steps below.

1. clone repo then open terminal

   - `docker-compose build`
   - `docker-compose up`
     > Now our API server start ...
   - `docker exec -it skyloov bash`
     > To accesses skyloov app container bash


   - `python3 -c 'import secrets; print(secrets.token_urlsafe(38))'` 
     > Generate a SecretKey
     > Please turn the DEBUG to False (if u wanna try the prod mode) in settings.py

2. After lunching the skyloov app container and got into it:

   - `python manage.py migrate`
   - `python manage.py createsuperuser`

   - > Enter the username and password for the admin pannel 



/products/search/?name=test1
/products/search/?brand=zz
/products/search/?category=a
/products/search/?min_price=0&max_price=100
/products/search/?min_quantity=0&max_quantity=10
/products/search/?created_at=2023-05-05
# Overview

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

## Skyloov :

  - ### This project is deployed on https://skyloov.youcefi-yassine.com using kubetnets

### Code challenge for Skyloov Property Portal, This is some of useful links for reviewing and testing the project :

- [Swagger documentation](https://skyloov.youcefi-yassine.com/swagger/)
- [redocs documentation](https://skyloov.youcefi-yassine.com/redocs/)

## Requirements

- [Docker file](https://github.com/yassine-youcefi/Skyloov/blob/main/Dockerfile)

  > Contain docker global config ...

- [Docker-compose](https://github.com/yassine-youcefi/Skyloov/blob/main/docker-compose.yml)

  > My docker containers configuration ...

- [requirements.txt](https://github.com/yassine-youcefi/Skyloov/blob/main/requirements.txt)

  > All python requirements ...

- `.env`

  > Project environment variables

<br>
<hr>
<br>

## Start-up

### Pleas follow the steps below.

<br>
1. clone repo then open terminal

```bash
docker-compose build
```

```bash
docker-compose up
```

  > Now our API server start ...
   > To accesses skyloov app container bash

```bash
docker exec -it skyloov bash
```

   > Generate a SecretKey
   > Please turn the DEBUG to False (if u wanna try the prod mode) in settings.py

```bash
python3 -c 'import secrets; print(secrets.token_urlsafe(38))'
```


<br>

2.After lunching the skyloov app container and got into it:
> To migrate the database
```bash
python manage.py migrate
```
> To collect static files
```bash
python manage.py collectstatic
```

> Enter the username and password for the admin pannel
```bash
python manage.py createsuperuser
```


<br>

3.If you want to run the tests:

```bash
pytest
```

<br>
<hr>
<br>

# Connect Application :

### End-point : connect token

- For obtaining a token we should send a POST request to API. Request body must have two parts : username and password.

#### Method: POST

<https://skyloov.youcefi-yassine.com/connect/token/>

#### Headers

| Content-Type | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

#### Body (**raw**)

```json
{
  "username": "string",
  "password": "string"
}
```

#### Response (**raw**) 200

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point : connect verify token

- For verify a token we should send a POST request to API. Request body must have two parts : token.

#### Method: POST

<https://skyloov.youcefi-yassine.com/connect/api/token/verify/>

#### Headers

| Content-Type | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

#### Body (**raw**)

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
}
```

#### Response (**raw**) 200

``

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: connect token refresh

- To refresh the JWT token, you can send a POST request to the token refresh endpoint with the refresh token in the request body.

#### Method: GET

<https://skyloov.youcefi-yassine.com/connect/token/refresh/>

#### Body (**raw**)

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Response (**raw**) 200

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point : connect signup

- Signup endpoit, allow user registration

#### Method: POST

<https://skyloov.youcefi-yassine.com/connect/signup/>

#### Body (**raw**)

```json
{
  "username": "string",
  "password": "string",
  "email": "string@gmail.com"
}
```

#### Response (**raw**) 200

```json
{
  "username": "string",
  "password": "string",
  "email": "string@gmail.com"
}
```

- NOTE : After the registration, the user will receive the bellow email :

  ![alt text](email.png)

<br>
<hr>
<br>

# Products Application :

### End-point: products search

#### Method: GET

<https://skyloov.youcefi-yassine.com/products/search/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

> NOTE: This view return paginated response, 20 products per page.

#### Response (**raw**)

- The response will look like this for example:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "test",
      "brand": "test",
      "description": "test",
      "category": "test",
      "price": "0.00",
      "quantity": 1,
      "image": "https://skyloov.youcefi-yassine.com/media/products/email_lX1jyrd.png",
      "image_thumbnail": "https://skyloov.youcefi-yassine.com/media/products/test_thumb_uo2fXhN.jpg",
      "rating": 5.0,
      "created_at": "2023-05-06",
      "updated_at": "2023-05-06"
    }
  ]
}
```

- Here are some sample GET requests for each field :

  - name :

    <https://skyloov.youcefi-yassine.com/products/search/?name=test>

  - brand :

    <https://skyloov.youcefi-yassine.com/products/search/?brand=test>

  - category :

    <https://skyloov.youcefi-yassine.com/products/search/?category=test>

  - price :

    <https://skyloov.youcefi-yassine.com/products/search/?min_price=0&max_price=100>

  - quantity :

    <https://skyloov.youcefi-yassine.com/products/search/?min_quantity=0&max_quantity=10>

  - rating :

    <https://skyloov.youcefi-yassine.com/products/search/?rating=5>

  - created_at :

    <https://skyloov.youcefi-yassine.com/products/search/?created_at=2023-05-05>

- You can also sort the results :
  <https://skyloov.youcefi-yassine.com/products/search/?sort=name>


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


### End-point: products create

#### Method: POST

<https://skyloov.youcefi-yassine.com/products/create/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Body (**raw**)

- you need to pass the product id in the items list

```json
{
  "name": "string",
  "brand": "string",
  "description": "string",
  "category": "string",
  "price": "decimal",
  "quantity": "integer",
  "rating": "number"
}
```

#### Response (**raw**) 200

```json
{
  "id": 8,
  "created_at": "2023/05/10",
  "updated_at": "2023/05/10",
  "name": "string",
  "brand": "string",
  "description": "string",
  "category": "string",
  "price": "10.00",
  "quantity": 5,
  "image": null,
  "image_thumbnail": null,
  "rating": 2.0
}
```  



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: products image upload

#### Method: PUT

<https://skyloov.youcefi-yassine.com/products/4/image_upload/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Body (**raw**)

- you need to pass the product id in the items list

```json
{
  "image": "file",
}
```

#### Response (**raw**) 200

```json
{
    "success": "Image uploaded successfully"
}
```  


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: cart list

#### Method: GET

<https://skyloov.youcefi-yassine.com/products/cart/all/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

> NOTE: This view return paginated response, 20 products per page.
> The returned carts responses are bellow to the request user

#### Response (**raw**)

- The response will look like this for example:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 8,
            "status": "OPEN",
            "total": 2.0,
            "items": [
                {
                    "id": 2,
                    "created_at": "2023/05/06",
                    "updated_at": "2023/05/06",
                    "name": "string",
                    "brand": "string",
                    "description": "string",
                    "category": "string",
                    "price": "2.00",
                    "quantity": 0,
                    "image": null,
                    "rating": 0.0
                }
            ],
            "created_at": "2023-05-07T20:15:06.872987Z",
            "updated_at": "2023-05-07T20:15:06.873015Z"
        },
        ...
    ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: cart details

#### Method: GET

<https://skyloov.youcefi-yassine.com/products/cart/8/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

> NOTE: This view return paginated response, 20 products per page.
> The returned carts responses are bellow to the request user

#### Response (**raw**)

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 8,
            "status": "OPEN",
            "total": 2.0,
            "items": [
                {
                    "id": 2,
                    "created_at": "2023/05/06",
                    "updated_at": "2023/05/06",
                    "name": "string",
                    "brand": "string",
                    "description": "string",
                    "category": "string",
                    "price": "2.00",
                    "quantity": 0,
                    "image": null,
                    "rating": 0.0
                }
            ],
            "created_at": "2023-05-07T20:15:06.872987Z",
            "updated_at": "2023-05-07T20:15:06.873015Z"
        },
        ...
    ]
}
```

#### Method: post

<https://skyloov.youcefi-yassine.com/products/cart/create/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Body (**raw**)

- you need to pass the product id in the items list

```json
{
  "items": [2]
}
```

#### Response (**raw**)

```json
{
  "id": 8,
  "status": "OPEN",
  "total": 2.0,
  "items": [
    {
      "id": 2,
      "created_at": "2023/05/06",
      "updated_at": "2023/05/06",
      "name": "string",
      "brand": "string",
      "description": "string",
      "category": "string",
      "price": "2.00",
      "quantity": 0,
      "image": null,
      "rating": 0.0
    }
  ],
  "created_at": "2023-05-07T20:15:06.872987Z",
  "updated_at": "2023-05-07T20:15:06.873015Z"
}
```

#### Method: DELETE

<https://skyloov.youcefi-yassine.com/products/cart/8/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Response 204

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

### End-point: cart items

#### Method: GET

<https://skyloov.youcefi-yassine.com/products/cart/8/items/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Response (**raw**) 200

```json
{
  "items": [2]
}
```

#### Method: PUT

<https://skyloov.youcefi-yassine.com/products/cart/8/items/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Body (**raw**)

- you need to pass the product id in the items list, to update your cart items

```json
{
  "items": [1, 2]
}
```

#### Response (**raw**) 200

```json
{
  "items": [1, 2]
}
```

#### Method: DELETE

<https://skyloov.youcefi-yassine.com/products/cart/8/items/>

#### 🔑 Authentication bearer

| Param | value        | Type   |
| ----- | ------------ | ------ |
| token | <your_token> | berear |

#### Body (**raw**)

- you need to pass the product id in the items list, to update your cart items

```json
{
  "items": [2]
}
```

#### Response 204

```json
{
  "items": [1]
}
```

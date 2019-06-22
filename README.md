# test_accounts
Testing accounts and social auth Django


## API

## Token Authentication

## JWT Authentication

`pip install djangorestframework_simplejwt` and add authentication class to backend:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ...
    )
}
```

Create the views to obtain and refresh the token that will be received after authentication with username/password.

```
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^api/v1/auth/token/$', obtain_jwt_token, name='obtain_token'),
    url(r'^api/v1/auth/token-refresh/$', obtain_jwt_token, name='refresh_token'),
]

```

With a POST request we can get the token:

```
POST http://127.0.0.1:8000/api/v1/auth/token/ HTTP/1.1
Content-Type: application/json

{
    "email": "zadigo@gmail.com",
    "password": "touparet"
}

{
  "token": "..."
}
```

In order to access the protected views on the backend, we should include the access token in the header of all requests:

```
GET http://127.0.0.1:8000/api/v1/users/ HTTP/1.1
Authorization: JWT __token__

```
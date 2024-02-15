# Authentication

```python
authentication_controller = client.authentication
```

## Class Name

`AuthenticationController`

## Methods

* [O Auth Bearer Token](../../doc/controllers/authentication.md#o-auth-bearer-token)
* [Custom Authentication](../../doc/controllers/authentication.md#custom-authentication)
* [Custom Query or Header Authentication](../../doc/controllers/authentication.md#custom-query-or-header-authentication)
* [O Auth Grant Types or Combinations](../../doc/controllers/authentication.md#o-auth-grant-types-or-combinations)
* [No Auth](../../doc/controllers/authentication.md#no-auth)
* [O Auth Client Credentials Grant](../../doc/controllers/authentication.md#o-auth-client-credentials-grant)
* [Basic Auth and Api Header Auth](../../doc/controllers/authentication.md#basic-auth-and-api-header-auth)
* [O Auth Authorization Grant](../../doc/controllers/authentication.md#o-auth-authorization-grant)
* [Multiple Auth Combination](../../doc/controllers/authentication.md#multiple-auth-combination)


# O Auth Bearer Token

```python
def o_auth_bearer_token(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.o_auth_bearer_token()
print(result)
```


# Custom Authentication

```python
def custom_authentication(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.custom_authentication()
print(result)
```


# Custom Query or Header Authentication

```python
def custom_query_or_header_authentication(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.custom_query_or_header_authentication()
print(result)
```


# O Auth Grant Types or Combinations

This endpoint tests or combinations of OAuth types

```python
def o_auth_grant_types_or_combinations(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.o_auth_grant_types_or_combinations()
print(result)
```


# No Auth

**This endpoint is deprecated since version 0.0.1-alpha. You should not use this method as it requires no auth and can bring security issues to the server and api call itself!!**

This endpoint does not use auth.

Swagger URL Endpoint 1: [http://swagger.io/endpoint1](http://swagger.io/endpoint1)

:information_source: **Note** This endpoint does not require authentication.

```python
def no_auth(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.no_auth()
print(result)
```


# O Auth Client Credentials Grant

```python
def o_auth_client_credentials_grant(self)
```

## Response Type

[`ServiceStatus`](../../doc/models/service-status.md)

## Example Usage

```python
result = authentication_controller.o_auth_client_credentials_grant()
print(result)
```


# Basic Auth and Api Header Auth

```python
def basic_auth_and_api_header_auth(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.basic_auth_and_api_header_auth()
print(result)
```


# O Auth Authorization Grant

```python
def o_auth_authorization_grant(self)
```

## Response Type

[`User`](../../doc/models/user.md)

## Example Usage

```python
result = authentication_controller.o_auth_authorization_grant()
print(result)
```


# Multiple Auth Combination

**This endpoint is deprecated.**

This endpoint uses globally applied auth which is a hypothetical scneraio but covers the worst case.

Swagger URL Endpoint 1: [http://swagger.io/endpoint1](http://swagger.io/endpoint1)

```python
def multiple_auth_combination(self)
```

## Response Type

`str`

## Example Usage

```python
result = authentication_controller.multiple_auth_combination()
print(result)
```


# O Auth Authorization

```python
o_auth_authorization_controller = client.o_auth_authorization
```

## Class Name

`OAuthAuthorizationController`

## Methods

* [Request Token O Auth CCG](../../doc/controllers/o-auth-authorization.md#request-token-o-auth-ccg)
* [Request Token O Auth ACG](../../doc/controllers/o-auth-authorization.md#request-token-o-auth-acg)
* [Refresh Token O Auth ACG](../../doc/controllers/o-auth-authorization.md#refresh-token-o-auth-acg)
* [Request Token O Auth ROPCG](../../doc/controllers/o-auth-authorization.md#request-token-o-auth-ropcg)
* [Refresh Token O Auth ROPCG](../../doc/controllers/o-auth-authorization.md#refresh-token-o-auth-ropcg)


# Request Token O Auth CCG

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_o_auth_ccg(self,
                            authorization,
                            scope=None,
                            _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.request_token_o_auth_ccg(
    authorization,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |


# Request Token O Auth ACG

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_o_auth_acg(self,
                            authorization,
                            code,
                            redirect_uri,
                            _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `code` | `str` | Form, Required | Authorization Code |
| `redirect_uri` | `str` | Form, Required | Redirect Uri |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

code = 'code8'

redirect_uri = 'redirect_uri8'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.request_token_o_auth_acg(
    authorization,
    code,
    redirect_uri,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |


# Refresh Token O Auth ACG

Obtain a new access token using a refresh token

:information_source: **Note** This endpoint does not require authentication.

```python
def refresh_token_o_auth_acg(self,
                            authorization,
                            refresh_token,
                            scope=None,
                            _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `refresh_token` | `str` | Form, Required | Refresh token |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

refresh_token = 'refresh_token0'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.refresh_token_o_auth_acg(
    authorization,
    refresh_token,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |


# Request Token O Auth ROPCG

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_o_auth_ropcg(self,
                              authorization,
                              username,
                              password,
                              scope=None,
                              _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `username` | `str` | Form, Required | Resource owner username |
| `password` | `str` | Form, Required | Resource owner password |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

username = 'username0'

password = 'password4'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.request_token_o_auth_ropcg(
    authorization,
    username,
    password,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |


# Refresh Token O Auth ROPCG

Obtain a new access token using a refresh token

:information_source: **Note** This endpoint does not require authentication.

```python
def refresh_token_o_auth_ropcg(self,
                              authorization,
                              refresh_token,
                              scope=None,
                              _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `refresh_token` | `str` | Form, Required | Refresh token |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

refresh_token = 'refresh_token0'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.refresh_token_o_auth_ropcg(
    authorization,
    refresh_token,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |


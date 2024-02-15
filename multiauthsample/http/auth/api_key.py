# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.query_auth import QueryAuth


class ApiKey(QueryAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in ApiKey

        """
        return "ApiKey: token or api-key is undefined."

    def __init__(self, api_key_credentials):
        auth_params = {}
        if api_key_credentials is not None \
                and api_key_credentials.token is not None:
            auth_params["token"] = api_key_credentials.token
        if api_key_credentials is not None \
                and api_key_credentials.api_key is not None:
            auth_params["api-key"] = api_key_credentials.api_key
        super().__init__(auth_params=auth_params)


class ApiKeyCredentials:

    @property
    def token(self):
        return self._token

    @property
    def api_key(self):
        return self._api_key

    def __init__(self, token, api_key):
        if token is None:
            raise ValueError('token cannot be None')
        self._token = token
        if api_key is None:
            raise ValueError('api_key cannot be None')
        self._api_key = api_key

    def clone_with(self, token=None, api_key=None):
        return ApiKeyCredentials(token or self.token, api_key or self.api_key)
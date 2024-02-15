# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from multiauthsample.api_helper import APIHelper
from multiauthsample.models.o_auth_token import OAuthToken
from apimatic_core.utilities.auth_helper import AuthHelper
from multiauthsample.controllers.o_auth_authorization_controller import\
    OAuthAuthorizationController


class OAuthCCG(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in OAuthCCG

        """
        return "OAuthCCG: OAuthToken is undefined or expired."

    def __init__(self, o_auth_ccg_credentials, config):
        auth_params = {}
        self._o_auth_client_id = o_auth_ccg_credentials.o_auth_client_id \
            if o_auth_ccg_credentials is not None else None
        self._o_auth_client_secret = o_auth_ccg_credentials.o_auth_client_secret \
            if o_auth_ccg_credentials is not None else None
        if o_auth_ccg_credentials is not None \
                and isinstance(o_auth_ccg_credentials.o_auth_token, OAuthToken):
            self._o_auth_token = OAuthToken.from_dictionary(
                APIHelper.to_dictionary(o_auth_ccg_credentials.o_auth_token))
        else:
            self._o_auth_token = o_auth_ccg_credentials.o_auth_token \
                if o_auth_ccg_credentials is not None else None
        self._o_auth_api = OAuthAuthorizationController(config)
        if isinstance(self._o_auth_token, OAuthToken) and hasattr(self._o_auth_token, 'access_token'):
            auth_params["Authorization"] = "Bearer {}".format(self._o_auth_token.access_token)
        super().__init__(auth_params=auth_params)

    def is_valid(self):
        return self._o_auth_token and not self.is_token_expired()

    def build_basic_auth_header(self):
        """ Builds the basic auth header for endpoints in the
            OAuth Authorization Controller.

        Returns:
            str: The value of the Authentication header.

        """
        return "Basic {}".format(AuthHelper.get_base64_encoded_value(
            self._o_auth_client_id, self._o_auth_client_secret))

    def fetch_token(self, additional_params=None):
        """ Authorizes the client.

            
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The OAuth token.

        """
        token = self._o_auth_api.request_token_o_auth_ccg(
            self.build_basic_auth_header(),
            _optional_form_parameters=additional_params
        )
        if hasattr(token, 'expires_in'):
            current_utc_timestamp = AuthHelper.get_current_utc_timestamp()
            token.expiry = AuthHelper.get_token_expiry(current_utc_timestamp, token.expires_in)
        return token

    def is_token_expired(self):
        """ Checks if OAuth token has expired.

        Returns:
            bool: True if OAuth token has expired, False otherwise.

        """
        return hasattr(self._o_auth_token, 'expiry') and AuthHelper.is_token_expired(
            self._o_auth_token.expiry)


class OAuthCCGCredentials:

    @property
    def o_auth_client_id(self):
        return self._o_auth_client_id

    @property
    def o_auth_client_secret(self):
        return self._o_auth_client_secret

    @property
    def o_auth_token(self):
        return self._o_auth_token

    def __init__(self, o_auth_client_id, o_auth_client_secret,
                 o_auth_token=None):
        if o_auth_client_id is None:
            raise ValueError('o_auth_client_id cannot be None')
        self._o_auth_client_id = o_auth_client_id
        if o_auth_client_secret is None:
            raise ValueError('o_auth_client_secret cannot be None')
        self._o_auth_client_secret = o_auth_client_secret
        self._o_auth_token = o_auth_token

    def clone_with(self, o_auth_client_id=None, o_auth_client_secret=None,
                   o_auth_token=None):
        return OAuthCCGCredentials(
            o_auth_client_id or self.o_auth_client_id,
            o_auth_client_secret or self.o_auth_client_secret,
            o_auth_token or self.o_auth_token)

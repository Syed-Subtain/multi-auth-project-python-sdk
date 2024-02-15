# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from multiauthsample.api_helper import APIHelper
from multiauthsample.configuration import Server
from multiauthsample.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from multiauthsample.http.http_method_enum import HttpMethodEnum
from multiauthsample.models.o_auth_token import OAuthToken
from multiauthsample.exceptions.o_auth_provider_exception import OAuthProviderException


class OAuthAuthorizationController(BaseController):

    """A Controller to access Endpoints in the multiauthsample API."""
    def __init__(self, config):
        super(OAuthAuthorizationController, self).__init__(config)

    def request_token_o_auth_ccg(self,
                                 authorization,
                                 scope=None,
                                 _optional_form_parameters=None):
        """Does a POST request to /request_token.

        Create a new OAuth 2 token.

        Args:
            authorization (str): Authorization header in Basic auth format
            scope (str, optional): Requested scopes as a space-delimited
                list.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.AUTH)
            .path('/request_token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('client_credentials'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .form_param(Parameter()
                        .key('scope')
                        .value(scope))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()

    def request_token_o_auth_acg(self,
                                 authorization,
                                 code,
                                 redirect_uri,
                                 _optional_form_parameters=None):
        """Does a POST request to /oauth2/non-auth-server/token.

        Create a new OAuth 2 token.

        Args:
            authorization (str): Authorization header in Basic auth format
            code (str): Authorization Code
            redirect_uri (str): Redirect Uri
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/oauth2/non-auth-server/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('authorization_code'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .form_param(Parameter()
                        .key('code')
                        .value(code))
            .form_param(Parameter()
                        .key('redirect_uri')
                        .value(redirect_uri))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()

    def refresh_token_o_auth_acg(self,
                                 authorization,
                                 refresh_token,
                                 scope=None,
                                 _optional_form_parameters=None):
        """Does a POST request to /oauth2/non-auth-server/token.

        Obtain a new access token using a refresh token

        Args:
            authorization (str): Authorization header in Basic auth format
            refresh_token (str): Refresh token
            scope (str, optional): Requested scopes as a space-delimited
                list.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/oauth2/non-auth-server/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('refresh_token'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .form_param(Parameter()
                        .key('refresh_token')
                        .value(refresh_token))
            .form_param(Parameter()
                        .key('scope')
                        .value(scope))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()

    def request_token_o_auth_ropcg(self,
                                   authorization,
                                   username,
                                   password,
                                   scope=None,
                                   _optional_form_parameters=None):
        """Does a POST request to /oauth2/non-auth-server/token.

        Create a new OAuth 2 token.

        Args:
            authorization (str): Authorization header in Basic auth format
            username (str): Resource owner username
            password (str): Resource owner password
            scope (str, optional): Requested scopes as a space-delimited
                list.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/oauth2/non-auth-server/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('password'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .form_param(Parameter()
                        .key('username')
                        .value(username))
            .form_param(Parameter()
                        .key('password')
                        .value(password))
            .form_param(Parameter()
                        .key('scope')
                        .value(scope))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()

    def refresh_token_o_auth_ropcg(self,
                                   authorization,
                                   refresh_token,
                                   scope=None,
                                   _optional_form_parameters=None):
        """Does a POST request to /oauth2/non-auth-server/token.

        Obtain a new access token using a refresh token

        Args:
            authorization (str): Authorization header in Basic auth format
            refresh_token (str): Refresh token
            scope (str, optional): Requested scopes as a space-delimited
                list.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/oauth2/non-auth-server/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value('refresh_token'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .form_param(Parameter()
                        .key('refresh_token')
                        .value(refresh_token))
            .form_param(Parameter()
                        .key('scope')
                        .value(scope))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OAuthToken.from_dictionary)
            .local_error('400', 'OAuth 2 provider returned an error.', OAuthProviderException)
            .local_error('401', 'OAuth 2 provider says client authentication failed.', OAuthProviderException)
        ).execute()
# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from multiauthsample.api_helper import APIHelper
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0
    TESTING = 1


class Server(Enum):
    """An enum for API servers"""
    DEFAULT = 0
    AUTH = 1


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def port(self):
        return self._port

    @property
    def suites(self):
        return self._suites

    @property
    def basic_auth_credentials(self):
        return self._basic_auth_credentials

    @property
    def api_key_credentials(self):
        return self._api_key_credentials

    @property
    def api_header_credentials(self):
        return self._api_header_credentials

    @property
    def o_auth_ccg_credentials(self):
        return self._o_auth_ccg_credentials

    @property
    def o_auth_acg_credentials(self):
        return self._o_auth_acg_credentials

    @property
    def o_auth_ropcg_credentials(self):
        return self._o_auth_ropcg_credentials

    @property
    def o_auth_bearer_token_credentials(self):
        return self._o_auth_bearer_token_credentials

    @property
    def custom_auth_credentials(self):
        return self._custom_auth_credentials

    @property
    def access_token(self):
        return self._access_token

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.TESTING, port='80', suites=1,
                 basic_auth_credentials=None, api_key_credentials=None,
                 api_header_credentials=None, o_auth_ccg_credentials=None,
                 o_auth_acg_credentials=None, o_auth_ropcg_credentials=None,
                 o_auth_bearer_token_credentials=None,
                 custom_auth_credentials=None, access_token=''):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance, override_http_client_configuration, http_call_back, timeout, max_retries,
                         backoff_factor, retry_statuses, retry_methods)

        # Current API environment
        self._environment = environment

        # port value
        self._port = port

        # suites value
        self._suites = suites

        # The object holding Basic Authentication credentials
        self._basic_auth_credentials = basic_auth_credentials

        # The object holding Custom Query Parameter credentials
        self._api_key_credentials = api_key_credentials

        # The object holding Custom Header Signature credentials
        self._api_header_credentials = api_header_credentials

        # The object holding OAuth 2 Client Credentials Grant credentials
        self._o_auth_ccg_credentials = o_auth_ccg_credentials

        # The object holding OAuth 2 Authorization Code Grant credentials
        self._o_auth_acg_credentials = o_auth_acg_credentials

        # The object holding OAuth 2 Resource Owner Credentials Grant credentials
        self._o_auth_ropcg_credentials = o_auth_ropcg_credentials

        # The object holding OAuth 2 Bearer token credentials
        self._o_auth_bearer_token_credentials = o_auth_bearer_token_credentials

        # The object holding Custom Authentication credentials
        self._custom_auth_credentials = custom_auth_credentials

        # TODO: Replace
        self._access_token = access_token

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   port=None, suites=None, basic_auth_credentials=None,
                   api_key_credentials=None, api_header_credentials=None,
                   o_auth_ccg_credentials=None, o_auth_acg_credentials=None,
                   o_auth_ropcg_credentials=None,
                   o_auth_bearer_token_credentials=None,
                   custom_auth_credentials=None, access_token=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        port = port or self.port
        suites = suites or self.suites
        basic_auth_credentials = basic_auth_credentials or self.basic_auth_credentials
        api_key_credentials = api_key_credentials or self.api_key_credentials
        api_header_credentials = api_header_credentials or self.api_header_credentials
        o_auth_ccg_credentials = o_auth_ccg_credentials or self.o_auth_ccg_credentials
        o_auth_acg_credentials = o_auth_acg_credentials or self.o_auth_acg_credentials
        o_auth_ropcg_credentials = o_auth_ropcg_credentials or self.o_auth_ropcg_credentials
        o_auth_bearer_token_credentials = o_auth_bearer_token_credentials or self.o_auth_bearer_token_credentials
        custom_auth_credentials = custom_auth_credentials or self.custom_auth_credentials
        access_token = access_token or self.access_token
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, port=port, suites=suites,
            basic_auth_credentials=basic_auth_credentials,
            api_key_credentials=api_key_credentials,
            api_header_credentials=api_header_credentials,
            o_auth_ccg_credentials=o_auth_ccg_credentials,
            o_auth_acg_credentials=o_auth_acg_credentials,
            o_auth_ropcg_credentials=o_auth_ropcg_credentials,
            o_auth_bearer_token_credentials=o_auth_bearer_token_credentials,
            custom_auth_credentials=custom_auth_credentials,
            access_token=access_token
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'http://apimatic.hopto.org:{suites}',
            Server.AUTH: 'http://apimaticauth.hopto.org:3000'
        },
        Environment.TESTING: {
            Server.DEFAULT: 'http://localhost:3000',
            Server.AUTH: 'http://localhost:3000/oauth2/auth-server'
        }
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "port": {'value': self.port, 'encode': False},
            "suites": {'value': self.suites, 'encode': False},
        }

        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters
        )

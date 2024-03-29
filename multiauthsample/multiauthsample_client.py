# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from multiauthsample.configuration import Configuration
from multiauthsample.controllers.base_controller import BaseController
from multiauthsample.configuration import Environment
from multiauthsample.http.auth.basic_auth import BasicAuth
from multiauthsample.http.auth.api_key import ApiKey
from multiauthsample.http.auth.api_header import ApiHeader
from multiauthsample.http.auth.o_auth_ccg import OAuthCCG
from multiauthsample.http.auth.o_auth_acg import OAuthACG
from multiauthsample.http.auth.o_auth_ropcg import OAuthROPCG
from multiauthsample.http.auth.o_auth_bearer_token import OAuthBearerToken
from multiauthsample.http.auth.custom_auth import CustomAuth
from multiauthsample.controllers.authentication_controller\
    import AuthenticationController
from multiauthsample.controllers.o_auth_authorization_controller\
    import OAuthAuthorizationController


class MultiauthsampleClient(object):
    @LazyProperty
    def authentication(self):
        return AuthenticationController(self.global_configuration)

    @LazyProperty
    def o_auth_authorization(self):
        return OAuthAuthorizationController(self.global_configuration)

    @property
    def o_auth_ccg(self):
        return self.auth_managers['OAuthCCG']

    @property
    def o_auth_acg(self):
        return self.auth_managers['OAuthACG']

    @property
    def o_auth_ropcg(self):
        return self.auth_managers['OAuthROPCG']

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.TESTING, port='80', suites=1,
                 basic_auth_credentials=None, api_key_credentials=None,
                 api_header_credentials=None, o_auth_ccg_credentials=None,
                 o_auth_acg_credentials=None, o_auth_ropcg_credentials=None,
                 o_auth_bearer_token_credentials=None,
                 custom_auth_credentials=None, access_token='', config=None):
        self.config = config or Configuration(
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
            access_token=access_token)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())\
            .global_header('accessToken', self.config.access_token)

        self.auth_managers = {key: None for key in ['basicAuth', 'apiKey',
                                                    'apiHeader', 'OAuthCCG',
                                                    'OAuthACG', 'OAuthROPCG',
                                                    'OAuthBearerToken',
                                                    'CustomAuth']}
        self.auth_managers['basicAuth'] = BasicAuth(
            self.config.basic_auth_credentials)
        self.auth_managers['apiKey'] = ApiKey(self.config.api_key_credentials)
        self.auth_managers['apiHeader'] = ApiHeader(
            self.config.api_header_credentials)
        self.auth_managers['OAuthCCG'] = OAuthCCG(
            self.config.o_auth_ccg_credentials, self.global_configuration)
        self.auth_managers['OAuthACG'] = OAuthACG(
            self.config.o_auth_acg_credentials, self.global_configuration)
        self.auth_managers['OAuthROPCG'] = OAuthROPCG(
            self.config.o_auth_ropcg_credentials, self.global_configuration)
        self.auth_managers['OAuthBearerToken'] = OAuthBearerToken(
            self.config.o_auth_bearer_token_credentials)
        self.auth_managers['CustomAuth'] = CustomAuth(self.config)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)


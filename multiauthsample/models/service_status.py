# -*- coding: utf-8 -*-

"""
multiauthsample

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from multiauthsample.api_helper import APIHelper


class ServiceStatus(object):

    """Implementation of the 'ServiceStatus' model.

    TODO: type model description here.

    Attributes:
        app (str): TODO: type description here.
        moto (str): TODO: type description here.
        notes (int): TODO: type description here.
        users (int): TODO: type description here.
        time (str): TODO: type description here.
        os (str): TODO: type description here.
        php_version (str): TODO: type description here.
        status (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "app": 'app',
        "moto": 'moto',
        "notes": 'notes',
        "users": 'users',
        "time": 'time',
        "os": 'os',
        "php_version": 'php_version'
    }

    _optionals = [
        'app',
        'moto',
        'notes',
        'users',
        'time',
        'os',
        'php_version',
    ]

    def __init__(self,
                 status=None,
                 app=APIHelper.SKIP,
                 moto=APIHelper.SKIP,
                 notes=APIHelper.SKIP,
                 users=APIHelper.SKIP,
                 time=APIHelper.SKIP,
                 os=APIHelper.SKIP,
                 php_version=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ServiceStatus class"""

        # Initialize members of the class
        if app is not APIHelper.SKIP:
            self.app = app 
        if moto is not APIHelper.SKIP:
            self.moto = moto 
        if notes is not APIHelper.SKIP:
            self.notes = notes 
        if users is not APIHelper.SKIP:
            self.users = users 
        if time is not APIHelper.SKIP:
            self.time = time 
        if os is not APIHelper.SKIP:
            self.os = os 
        if php_version is not APIHelper.SKIP:
            self.php_version = php_version 
        self.status = status 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        status = dictionary.get("status") if dictionary.get("status") else None
        app = dictionary.get("app") if dictionary.get("app") else APIHelper.SKIP
        moto = dictionary.get("moto") if dictionary.get("moto") else APIHelper.SKIP
        notes = dictionary.get("notes") if dictionary.get("notes") else APIHelper.SKIP
        users = dictionary.get("users") if dictionary.get("users") else APIHelper.SKIP
        time = dictionary.get("time") if dictionary.get("time") else APIHelper.SKIP
        os = dictionary.get("os") if dictionary.get("os") else APIHelper.SKIP
        php_version = dictionary.get("php_version") if dictionary.get("php_version") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(status,
                   app,
                   moto,
                   notes,
                   users,
                   time,
                   os,
                   php_version,
                   dictionary)

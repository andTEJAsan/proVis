# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserRegister(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, email_id: str=None, password: str=None):  # noqa: E501
        """UserRegister - a model defined in Swagger

        :param name: The name of this UserRegister.  # noqa: E501
        :type name: str
        :param email_id: The email_id of this UserRegister.  # noqa: E501
        :type email_id: str
        :param password: The password of this UserRegister.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'name': str,
            'email_id': str,
            'password': str
        }

        self.attribute_map = {
            'name': 'name',
            'email_id': 'email_id',
            'password': 'password'
        }
        self._name = name
        self._email_id = email_id
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserRegister':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserRegister of this UserRegister.  # noqa: E501
        :rtype: UserRegister
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this UserRegister.


        :return: The name of this UserRegister.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserRegister.


        :param name: The name of this UserRegister.
        :type name: str
        """

        self._name = name

    @property
    def email_id(self) -> str:
        """Gets the email_id of this UserRegister.


        :return: The email_id of this UserRegister.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id: str):
        """Sets the email_id of this UserRegister.


        :param email_id: The email_id of this UserRegister.
        :type email_id: str
        """

        self._email_id = email_id

    @property
    def password(self) -> str:
        """Gets the password of this UserRegister.


        :return: The password of this UserRegister.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserRegister.


        :param password: The password of this UserRegister.
        :type password: str
        """

        self._password = password

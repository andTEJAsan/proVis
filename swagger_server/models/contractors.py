# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Contractors(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, contractor_id: str=None, name: str=None, email: str=None, address: str=None, phone_no: str=None, company_id: str=None):  # noqa: E501
        """Contractors - a model defined in Swagger

        :param contractor_id: The contractor_id of this Contractors.  # noqa: E501
        :type contractor_id: str
        :param name: The name of this Contractors.  # noqa: E501
        :type name: str
        :param email: The email of this Contractors.  # noqa: E501
        :type email: str
        :param address: The address of this Contractors.  # noqa: E501
        :type address: str
        :param phone_no: The phone_no of this Contractors.  # noqa: E501
        :type phone_no: int
        :param company_id: The company_id of this Contractors.  # noqa: E501
        :type company_id: str
        """
        self.swagger_types = {
            'contractor_id': str,
            'name': str,
            'email': str,
            'address': str,
            'phone_no': str,
            'company_id': str
        }

        self.attribute_map = {
            'contractor_id': 'contractor_id',
            'name': 'name',
            'email': 'email',
            'address': 'address',
            'phone_no': 'phone_no',
            'company_id': 'company_id'
        }
        self._contractor_id = contractor_id
        self._name = name
        self._email = email
        self._address = address
        self._phone_no = phone_no
        self._company_id = company_id

    @classmethod
    def from_dict(cls, dikt) -> 'Contractors':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Contractors of this Contractors.  # noqa: E501
        :rtype: Contractors
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contractor_id(self) -> str:
        """Gets the contractor_id of this Contractors.


        :return: The contractor_id of this Contractors.
        :rtype: str
        """
        return self._contractor_id

    @contractor_id.setter
    def contractor_id(self, contractor_id: str):
        """Sets the contractor_id of this Contractors.


        :param contractor_id: The contractor_id of this Contractors.
        :type contractor_id: str
        """

        self._contractor_id = contractor_id

    @property
    def name(self) -> str:
        """Gets the name of this Contractors.


        :return: The name of this Contractors.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Contractors.


        :param name: The name of this Contractors.
        :type name: str
        """

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this Contractors.


        :return: The email of this Contractors.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Contractors.


        :param email: The email of this Contractors.
        :type email: str
        """

        self._email = email

    @property
    def address(self) -> str:
        """Gets the address of this Contractors.


        :return: The address of this Contractors.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Contractors.


        :param address: The address of this Contractors.
        :type address: str
        """

        self._address = address

    @property
    def phone_no(self) -> str:
        """Gets the phone_no of this Contractors.


        :return: The phone_no of this Contractors.
        :rtype: int
        """
        return self._phone_no

    @phone_no.setter
    def phone_no(self, phone_no: str):
        """Sets the phone_no of this Contractors.


        :param phone_no: The phone_no of this Contractors.
        :type phone_no: int
        """

        self._phone_no = phone_no

    @property
    def company_id(self) -> str:
        """Gets the company_id of this Contractors.


        :return: The company_id of this Contractors.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: str):
        """Sets the company_id of this Contractors.


        :param company_id: The company_id of this Contractors.
        :type company_id: str
        """

        self._company_id = company_id

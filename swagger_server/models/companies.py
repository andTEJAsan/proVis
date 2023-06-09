# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Companies(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, company_id: str=None, name: str=None, company_img_url: str=None, about_us: str=None, website_link: str=None):  # noqa: E501
        """Companies - a model defined in Swagger

        :param company_id: The company_id of this Companies.  # noqa: E501
        :type company_id: str
        :param name: The name of this Companies.  # noqa: E501
        :type name: str
        :param company_img_url: The company_img_url of this Companies.  # noqa: E501
        :type company_img_url: str
        :param about_us: The about_us of this Companies.  # noqa: E501
        :type about_us: str
        :param website_link: The website_link of this Companies.  # noqa: E501
        :type website_link: str
        """
        self.swagger_types = {
            'company_id': str,
            'name': str,
            'company_img_url': str,
            'about_us': str,
            'website_link': str
        }

        self.attribute_map = {
            'company_id': 'company_id',
            'name': 'name',
            'company_img_url': 'company_img_url',
            'about_us': 'about_us',
            'website_link': 'website_link'
        }
        self._company_id = company_id
        self._name = name
        self._company_img_url = company_img_url
        self._about_us = about_us
        self._website_link = website_link

    @classmethod
    def from_dict(cls, dikt) -> 'Companies':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Companies of this Companies.  # noqa: E501
        :rtype: Companies
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_id(self) -> str:
        """Gets the company_id of this Companies.


        :return: The company_id of this Companies.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: str):
        """Sets the company_id of this Companies.


        :param company_id: The company_id of this Companies.
        :type company_id: str
        """

        self._company_id = company_id

    @property
    def name(self) -> str:
        """Gets the name of this Companies.


        :return: The name of this Companies.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Companies.


        :param name: The name of this Companies.
        :type name: str
        """

        self._name = name

    @property
    def company_img_url(self) -> str:
        """Gets the company_img_url of this Companies.


        :return: The company_img_url of this Companies.
        :rtype: str
        """
        return self._company_img_url

    @company_img_url.setter
    def company_img_url(self, company_img_url: str):
        """Sets the company_img_url of this Companies.


        :param company_img_url: The company_img_url of this Companies.
        :type company_img_url: str
        """

        self._company_img_url = company_img_url

    @property
    def about_us(self) -> str:
        """Gets the about_us of this Companies.


        :return: The about_us of this Companies.
        :rtype: str
        """
        return self._about_us

    @about_us.setter
    def about_us(self, about_us: str):
        """Sets the about_us of this Companies.


        :param about_us: The about_us of this Companies.
        :type about_us: str
        """

        self._about_us = about_us

    @property
    def website_link(self) -> str:
        """Gets the website_link of this Companies.


        :return: The website_link of this Companies.
        :rtype: str
        """
        return self._website_link

    @website_link.setter
    def website_link(self, website_link: str):
        """Sets the website_link of this Companies.


        :param website_link: The website_link of this Companies.
        :type website_link: str
        """

        self._website_link = website_link

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product_categories import ProductCategories  # noqa: F401,E501
from swagger_server.models.product_lists import ProductLists  # noqa: F401,E501
from swagger_server.models.product_locations import ProductLocations  # noqa: F401,E501
from swagger_server import util


class ProductApiResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, p_uid: str=None, location: ProductLocations=None, category: ProductCategories=None, product_list: ProductLists=None):  # noqa: E501
        """ProductApiResponse - a model defined in Swagger

        :param p_uid: The p_uid of this ProductApiResponse.  # noqa: E501
        :type p_uid: str
        :param location: The location of this ProductApiResponse.  # noqa: E501
        :type location: ProductLocations
        :param category: The category of this ProductApiResponse.  # noqa: E501
        :type category: ProductCategories
        :param product_list: The product_list of this ProductApiResponse.  # noqa: E501
        :type product_list: ProductLists
        """
        self.swagger_types = {
            'p_uid': str,
            'location': ProductLocations,
            'category': ProductCategories,
            'product_list': ProductLists
        }

        self.attribute_map = {
            'p_uid': 'p_uid',
            'location': 'location',
            'category': 'category',
            'product_list': 'product_list'
        }
        self._p_uid = p_uid
        self._location = location
        self._category = category
        self._product_list = product_list

    @classmethod
    def from_dict(cls, dikt) -> 'ProductApiResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProductApiResponse of this ProductApiResponse.  # noqa: E501
        :rtype: ProductApiResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_uid(self) -> str:
        """Gets the p_uid of this ProductApiResponse.


        :return: The p_uid of this ProductApiResponse.
        :rtype: str
        """
        return self._p_uid

    @p_uid.setter
    def p_uid(self, p_uid: str):
        """Sets the p_uid of this ProductApiResponse.


        :param p_uid: The p_uid of this ProductApiResponse.
        :type p_uid: str
        """

        self._p_uid = p_uid

    @property
    def location(self) -> ProductLocations:
        """Gets the location of this ProductApiResponse.


        :return: The location of this ProductApiResponse.
        :rtype: ProductLocations
        """
        return self._location

    @location.setter
    def location(self, location: ProductLocations):
        """Sets the location of this ProductApiResponse.


        :param location: The location of this ProductApiResponse.
        :type location: ProductLocations
        """

        self._location = location

    @property
    def category(self) -> ProductCategories:
        """Gets the category of this ProductApiResponse.


        :return: The category of this ProductApiResponse.
        :rtype: ProductCategories
        """
        return self._category

    @category.setter
    def category(self, category: ProductCategories):
        """Sets the category of this ProductApiResponse.


        :param category: The category of this ProductApiResponse.
        :type category: ProductCategories
        """

        self._category = category

    @property
    def product_list(self) -> ProductLists:
        """Gets the product_list of this ProductApiResponse.


        :return: The product_list of this ProductApiResponse.
        :rtype: ProductLists
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list: ProductLists):
        """Sets the product_list of this ProductApiResponse.


        :param product_list: The product_list of this ProductApiResponse.
        :type product_list: ProductLists
        """

        self._product_list = product_list

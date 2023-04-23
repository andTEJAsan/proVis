# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.products import Products  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_get_product(self):
        """Test case for get_product

        get a product by id
        """
        response = self.client.open(
            '/api//products/{queryid}'.format(queryid='queryid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_by_tags(self):
        """Test case for get_product_by_tags

        gets all products matching the tags
        """
        query_string = [('location', 'location_example'),
                        ('category', 'category_example')]
        response = self.client.open(
            '/api//products/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_products(self):
        """Test case for get_products

        get a list of all products
        """
        response = self.client.open(
            '/api//products',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_product(self):
        """Test case for post_product

        create a new product
        """
        body = Products()
        response = self.client.open(
            '/api//products',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

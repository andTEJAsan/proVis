# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.review_request import ReviewRequest  # noqa: E501
from swagger_server.models.reviews import Reviews  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReviewsController(BaseTestCase):
    """ReviewsController integration test stubs"""

    def test_products_queryid_reviews_get(self):
        """Test case for products_queryid_reviews_get

        get a list of all Reviews of a specific product
        """
        response = self.client.open(
            '/api//products/{queryid}/reviews'.format(queryid='queryid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_queryid_reviews_post(self):
        """Test case for products_queryid_reviews_post

        create a new review for a product with given id
        """
        body = ReviewRequest()
        response = self.client.open(
            '/api//products/{queryid}/reviews'.format(queryid='queryid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_queryid_reviews_reviewid_delete(self):
        """Test case for products_queryid_reviews_reviewid_delete

        deletes a specific product's review by id of both
        """
        response = self.client.open(
            '/api//products/{queryid}/reviews/{reviewid}'.format(queryid='queryid_example', reviewid='reviewid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

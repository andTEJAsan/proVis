import connexion
import six
import datetime

from swagger_server.models.orders import Orders  # noqa: E501
from swagger_server import util,db


def delete_customer_order(id, orderid):  # noqa: E501
    """deletes a specific customer&#x27;s order by id of both

    deletes a specific customer&#x27;s order by id of both # noqa: E501

    :param id: ID of customer whose orders need to be deleted
    :type id: str
    :param orderid: ID of order that needs to be deleted
    :type orderid: str

    :rtype: None
    """
    db.delete_customer_order(id,orderid)
    return 'do some magic!'


def get_customer_order(id, orderid):  # noqa: E501
    """get a customer&#x27;s specific order by id of both

    retrieves a specific order by id of customer and order # noqa: E501

    :param id: ID of customer whose orders need to be fetched
    :type id: str
    :param orderid: ID of order that needs to be fetched
    :type orderid: str

    :rtype: Orders
    """
    return db.get_customer_order(id,orderid)


def get_customer_orders(id):  # noqa: E501
    """get a list of all orders of a specific customers

    fetches all orders of a specific customer # noqa: E501

    :param id: ID of customer whose orders need to be fetched
    :type id: str

    :rtype: List[Orders]
    """
    return db.get_customer_orders 


def patch_customer_order(body, id, orderid):  # noqa: E501
    """update the details of a customer&#x27;s specific order by id of both

    updates the details of a customer&#x27;s order by passing parameters to be changed # noqa: E501

    :param body: updates a customer&#x27;s specific order
    :type body: dict | bytes
    :param id: ID of customer whose orders need to be updated
    :type id: str
    :param orderid: ID of order that needs to be updated
    :type orderid: str

    :rtype: Orders
    """
    if connexion.request.is_json:
        
        body = Orders.from_dict(connexion.request.get_json())  # noqa: E501

        db.patch_orderdate_orderid(body.order_date(),body.cus_ui().p_uid())
        db.patch_scheduling_status_orderid(body.scheduling_status().body.cus_id(),body.p_uid())
        db.patch_payment_status_orderid(body.payment_status(),body.cus_id(),body.p_uid())
        db.patch_exchangemail_orderid(body.exchange_emails(),body.cus_id(),body.p_uid()) 
    return body 


def post_order(body, id):  # noqa: E501
    """create a new order for a customer with given id

    create a new order for a customer with given id # noqa: E501

    :param body: creates a new order for a specific customer
    :type body: dict | bytes
    :param id: ID of customer for which new order is being added
    :type id: str

    :rtype: Orders
    """
    if connexion.request.is_json:

        body = Orders.from_dict(connexion.request.get_json())  # noqa: E501
        body.cus_uid(id=id)

    return db.post_order(body,id)

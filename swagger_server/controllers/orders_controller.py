import connexion
import six

from swagger_server.models.order_request import OrderRequest  # noqa: E501
from swagger_server.models.orders import Orders  # noqa: E501
from swagger_server import util,db


def get_customer_order(cusid, orderid):  # noqa: E501
    """get a customer&#x27;s specific order by id of both

    retrieves a specific order by id of customer and order # noqa: E501

    :param id: ID of customer whose orders need to be fetched
    :type id: str
    :param orderid: ID of order that needs to be fetched
    :type orderid: str

    :rtype: Orders
    """
    try:
        return db.getorder_fromid(cusid,orderid)
    except NameError:
        return  {"error":"Order with given order id doesn't exist","status":400}


def get_customer_orders(cusid):  # noqa: E501
    """get a list of all orders of a specific customers

    fetches all orders of a specific customer # noqa: E501

    :param id: ID of customer whose orders need to be fetched
    :type id: str

    :rtype: List[Orders]
    """
    return db.getorders_fromcusid(cusid)


def post_order(body):  # noqa: E501
    """create a new order for a customer with given id

    create a new order for a customer with given id # noqa: E501

    :param body: creates a new order for a specific customer
    :type body: dict | bytes
    :param id: ID of customer for which new order is being added
    :type id: str

    :rtype: Orders
    """
    if connexion.request.is_json:
        body = OrderRequest.from_dict(connexion.request.get_json())  # noqa: E501
        order=Orders(cus_uid=body._cus_uid,order_date_time=body._order_date_time,p_uid=body._p_uid,message=body._message)

        try:
            db.check_customer_exists(order.cus_uid)
        except NameError:
            return {"error":"Customer with given cus_uid doesn't exist","status":400}
        
        try:
            db.check_product_exists(order.p_uid)
        except NameError:
            return {"error":"Product with given p_uid doesn't exist","status":400}
        
        db.add_orders(order)

        return order


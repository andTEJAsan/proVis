import connexion
import six

from swagger_server.models.customers import Customers  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server import util,db


def delete_customer(id):  # noqa: E501
    """deletes a specific customer

    deletes a specific customer by id # noqa: E501

    :param id: ID of customer that needs to be deleted
    :type id: str

    :rtype: None
    """
    db.delete_customer(id)
    return 'do some magic!'


def get_customer(id):  # noqa: E501
    """get a customer by id

    retrieves a specific customer by id. # noqa: E501

    :param id: ID of customer that needs to be fetched
    :type id: str

    :rtype: Customers
    """
    return db.get_customer(id)


def get_customers():  # noqa: E501
    """get a list of all customers

    retrieves all customers. # noqa: E501


    :rtype: List[Customers]
    """
    return db.get_customers() 


def patch_customer(body, id):  # noqa: E501
    """update the details of a customer by id

    updates the details of a customer by passing parameters to be changed # noqa: E501

    :param body: updates a new customer
    :type body: dict | bytes
    :param id: ID of customer that needs to be updated
    :type id: str

    :rtype: Customers
    """
    if connexion.request.is_json:
        body = Customers.from_dict(connexion.request.get_json())  # noqa: E501
        db.patch_username_customerid(body.username(),id)
        db.patch_email_customerid(body.emailid(),id)
        db.patch_googleid_customerid(body.googleid(),id)
        db.patch_facebookid_customerid(body.facebookid(),id)
        db.patch_phone_customerid(body.phone_number(),id)
        db.patch_password_customerid(body.password(),id)
    return body

def post_customers(body):  # noqa: E501
    """create a new customer

    create a new customer given all details of customer while signing up # noqa: E501

    :param body: creates a new customer
    :type body: dict | bytes

    :rtype: LoginResponse
    """
    if connexion.request.is_json:
        body = Customers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

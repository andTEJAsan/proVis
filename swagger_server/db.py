from typing import Optional
import pymysql
import datetime

from swagger_server.models import Bookmarks,Companies,ContractorApiResponse
from swagger_server.models import Contractors,Customers,LoginResponse,LoginResponseInfo,Orders
from swagger_server.models import ProductAboutus,ProductApiResponse,ProductBusinesses,ProductCategories
from swagger_server.models import ProductLists, ProductLocations, ProductProfiles, ProductProjects
from swagger_server.models import Products,RegisterResponse,RegisterResponseInfo,UserLogin,UserRegister,VerifyEmail


connection = pymysql.connect(host='localhost',
                             user='newusr',
                             password='password',
                             database='tba',
                             cursorclass=pymysql.cursors.DictCursor)
def setup():
    """sets up the database"""
    with connection.cursor() as cursor :

        cursor.execute("""CREATE TABLE IF NOT EXISTS `customer` (
	`cus_uid` INT(6) NOT NULL AUTO_INCREMENT,
	`google_id` VARCHAR(255) DEFAULT NULL,
	`facebook_id` VARCHAR(255) DEFAULT NULL,
	`username` TEXT(255) NOT NULL,
	`email` VARCHAR(50) NOT NULL UNIQUE,
	`password` VARCHAR(255) NOT NULL,
	`phone` INT(20) DEFAULT NULL,
    `otp`   VARCHAR(255)  DEFAULT NULL,
	UNIQUE KEY `cus_id` (`cus_uid`) USING BTREE,
	PRIMARY KEY (`cus_uid`)
)""")
                       

        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_projects` (
	`id` INT(6) NOT NULL AUTO_INCREMENT,
	`project_img_url` VARCHAR(255) DEFAULT NULL,
	`project_name` VARCHAR(25) NOT NULL,
	`project_address` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_aboutus` (
	`id` INT(6) NOT NULL AUTO_INCREMENT,
	`description` TEXT(2000) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_category` (
	`id` INT(6) NOT NULL AUTO_INCREMENT,
	`name` TEXT(50) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `products` (
	`p_uid` INT(6) NOT NULL AUTO_INCREMENT,
	`p_category_id` INT(6) NOT NULL,
	`p_location_id` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`p_uid`) USING BTREE,
	PRIMARY KEY (`p_uid`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_location` (
	`id` INT(6) NOT NULL,
	`name` TEXT(100) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `company` (
	`company_uid` INT(6) NOT NULL,
	`name` TEXT(255) NOT NULL,
	`company_img_url` VARCHAR(255) DEFAULT NULL,
	`address` VARCHAR(300) DEFAULT NULL,
	UNIQUE KEY `id` (`company_uid`) USING BTREE,
	PRIMARY KEY (`company_uid`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_contractor` (
	`contractor_uid` INT(6) NOT NULL,
	`name` TEXT(255) NOT NULL,
	`email` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`contractor_uid`) USING BTREE,
	PRIMARY KEY (`contractor_uid`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `orders` (
	`id` INT(6) NOT NULL,
	`cus_uid` INT(6) NOT NULL,
	`order_date` VARCHAR(255) DEFAULT NULL,
	`p_uid` INT(6) NOT NULL,
	`payment_status` VARCHAR(255) DEFAULT NULL,
	`message` VARCHAR(500) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`cus_uid`) REFERENCES `customer` (`cus_uid`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`)
)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS `bookmarks` (
	`id` INT(6) NOT NULL,
	`cus_uid` INT(6) NOT NULL,
	`p_uid` INT(6) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`cus_uid`) REFERENCES `customer` (`cus_uid`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_business` (
	`id` INT(6) NOT NULL,
	`contractor_uid` INT(6) NOT NULL,
	`website_link` VARCHAR(255) DEFAULT NULL,
	`followers` INT(12) DEFAULT NULL,
	`address` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`contractor_uid`) REFERENCES `product_contractor` (`contractor_uid`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_profile` (
	`p_uid` INT(6) NOT NULL,
	`project_id` INT(6) DEFAULT NULL,
	`business_id` INT(6) DEFAULT NULL,
	`aboutus_id` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`p_uid`) USING BTREE,
	PRIMARY KEY (`p_uid`),
    FOREIGN KEY (`project_id`) REFERENCES `product_projects` (`id`),
    FOREIGN KEY (`aboutus_id`) REFERENCES `product_aboutus` (`id`)
)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS `product_list` (
	`id` INT(6) NOT NULL,
	`p_uid` INT(6) NOT NULL,
	`p_img_url` VARCHAR(255) DEFAULT NULL,
	`p_description` TEXT(500) DEFAULT NULL,
	`company_id` INT(6) DEFAULT NULL,
	`p_contractorid` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`),
    FOREIGN KEY (`company_id`) REFERENCES `company` (`company_uid`)
)""")
    
def delete_customer_bookmark(id : str,bookmarkid : str) -> None:
    """ delete bookmark(if exists) otherwise do nothing from bookmarks table having customer id = id and bookmarkid = bookmarkid"""
    with connection.cursor() as cursor:
        # Execute the delete query
        result = cursor.execute(
            "DELETE FROM `bookmarks` WHERE `cus_uid`=%s AND `id`=%s",
            (int(id), int(bookmarkid))
        )

        # Commit the transaction
        connection.commit()

def get_customer_bookmark(id :str,bookmarkid : str) -> Optional[Bookmarks]:
    """ from_dict function might be helpful"""
    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM `bookmarks` WHERE `cus_uid` = %s AND `id` = %s",
        (int(id), int(bookmarkid)),
    )
    result = cursor.fetchone()
    if result is None:
        return None
    return Bookmarks.from_dict({'id':str(result[0]),'cus_uid':str(result[1]),'p_uid':str(result[2])})
def get_customer_bookmarks(id:str) -> list[Bookmarks]:
    """get a list of all bookmarks of a specific customer

    fetches all bookmarks of a specific customer # noqa: E501

    :param id: ID of customer whose bookmark is needed
    :type id: str

    :rtype: List[Bookmarks]
    """
    """ you will get a list of dictionaries after querying from the database, don't forget to use from_dict()"""
    with connection.cursor() as cursor:
        cursor.execute(
           """SELECT * FROM `bookmarks` WHERE `cus_uid`=%s""" , int(id) 

        )
        results = cursor.fetchall()
        bookmarks = []
        for result in results :
            bookmarks.append(Bookmarks.from_dict({'id':str(result[0]),'cus_uid':str(result[1]),'p_uid':str(result[2])}))
    return bookmarks
def post_bookmark(bookmark: Bookmarks,id : str) -> None:
    """ add the bookmark in the list of bookmarks for given customer id"""
    assert bookmark.id() is None
    if bookmark.p_uid() is None:
        pass
def getpassword_fromemail(email_id : str) -> str:
    """fetch password from users database by email_id , return None if not there"""
    sql = """SELECT `password` from `customer` WHERE `email`=%s"""
    with connection.cursor() as cursor:
        cursor.execute(sql,(email_id))
        r = cursor.fetchone()
        if r is not None:
            password = r['password']
            return password
        return None
def getcusid_fromemail(email_id : str) -> str:
    """fetch cus_id from users database by email id, return None if not there"""
    sql = """SELECT `cus_uid` from `customer` WHERE `email`=%s"""
    with connection.cursor() as cursor:
        cursor.execute(sql,(email_id))
        r = cursor.fetchone()
        if r is not None:
            password = r["cus_uid"]
            return password
        return None
    
def getusername_fromemail(email_id:str) ->str:
    """fetch"""
    sql = """SELECT `username` from `customer` WHERE `email`=%s"""
    with connection.cursor() as cursor:
        cursor.execute(sql,(email_id))
        r = cursor.fetchone()
        if r is not None:
            username = r
            return username 
        return None
    
    pass
def delete_contractor(id : str) -> None:

    """delete contractor with contractor id = id"""
    pass
def get_username_fromcontractor(id : str) -> str:
    """get username as string from database"""
    pass
def get_email_fromcontractor(id : str) -> str:
    """get email of contractor from contractor id"""
    pass

def get_phone_fromcontractor(id : str) -> int:
    """get phone of contractor from contractor id"""
    pass

def get_address_fromcontractor(id : str) -> str:
    """get contractor adress from contractor id"""
    pass
def get_companies_fromcontractor(id : str) -> Companies:
    """get company from contractor id """
    pass
def get_apis_fromcontractor(id: str) -> list[ProductApiResponse]:
    """get list of ProductApiResponses from contractor id"""
    pass
def get_orders_fromcontractor(id : str) -> list[Orders]:
    """get list of Orders from contractor id"""
    pass
def patch_username_contractorid(username : str,id : str) -> None:
    """patch the username of the contractor with contractor_id = id to username"""
    pass
def patch_email_contractorid(email : str,id : str) -> None:
    pass
def patch_phone_contractorid(phone : int,id : str) -> None:
    pass
def patch_address_contractorid(address: str,id : str) -> None:
    pass
def patch_company_contractorid(company: Companies,id : str) -> None:
    pass
def patch_product_contractorid(products: list[ProductApiResponse],id : str) -> None:
    pass
def patch_orders_contractorid(orders: list[Orders],id : str) -> None:
    pass
def post_contractor(body : ContractorApiResponse) -> None:
    """adds contractor to the database"""
    pass
def delete_customer(id : str)-> None:
    pass
def get_customers()-> list[Customers]:
    """return list of all customers"""
    pass
def get_customer(id : str) -> Customers:
    """return Customer given customer_id"""
    pass
def patch_username_customerid(username:str,id:str)->None:

    pass
def patch_email_customerid(email:str,id:str)->None:
    pass
def patch_googleid_customerid(googleid:str,id:str)-> None:
    pass
def patch_facebookid_customerid(facebook:str,id:str) -> None:
    pass
def patch_phone_customerid(phone_number:int,id:str)->None:
    pass

def patch_password_customerid(password:str,id:str)->None:
    pass
def delete_customer_order(cus_id:str,orderid:str)->None:
    """delets order of customer having customer id cus_id and orderid = orderid"""

    pass
def get_customer_order(cus_id:str,orderid:str)->Orders:

    """get order from cus_id, orderid"""
    pass
def get_customer_orders(cus_id:str) -> list[Orders]:
    
    """get all orders of a particular customer"""
    pass

def patch_orderdate_orderid(orderdate : datetime,cusid:str,orderid:str)->None:
    pass
def patch_scheduling_status_orderid(schedulingstates : str ,cusid:str,orderid:str)->None:
    pass
def patch_payment_status_orderid(payment_status: str,cusid:str,orderid:str)->None:
    pass
def patch_exchangemail_orderid(exchangemail:str,cusid:str,orderid:str)->None:
    pass
def post_order(order : Orders,cus_id:str) -> Orders:
    pass
    """adds order to the database with given cus_id"""
def delete_product(ord_id:str)->None:
    """delete order from database with given order_id"""

    pass
def get_product(product_id:str)->ProductApiResponse:
    with cursor.connection() as cursor:
    #"""get order from database with given order_id"""
        p_uid = product_id
        sql = """SELECT * from `products` WHERE `p_uid`=%s"""
        cursor.execute(sql,(product_id))
        result = cursor.fetchone()
        if result is None:
            raise NameError
        ploc_id = result['p_location_id']
        pcat_id = result['p_category_id']
        sql = """SELECT * FROM `product_location` WHERE `id`=%s"""
        cursor.execute(sql,ploc_id)
        result = cursor.fetchone()
        location = ProductLocations.from_dict(result)
        sql="""SELECT * FROM `product_category` WHERE `id`=%s"""
        cursor.execute(sql,pcat_id)
        result=cursor.fetchone()
        category = ProductCategories.from_dict(result)
        sql="""SELECT * FROM `product_list` WHERE `p_uid`=%s"""
        cursor.execute(sql,(p_uid))
        result = cursor.fetchone()
        product_list = ProductLists.from_dict(result)
        return ProductApiResponse(p_uid=p_uid,location=location,category=category,product_list=product_list)


def get_product_by_tags(location:str,category:str) ->ProductApiResponse:
    if location is None:
        sql2 = """SELECT `id` FROM `product_location` WHERE `name`=%s"""

    pass

def get_products()->list[ProductApiResponse]:
    """return all products of a given order_id"""
    lr=[]
    with connection.cursor() as cursor:
        sql="""SELECT * FROM `products`"""
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            p_uid = result['p_uid']
            ploc_id = result['p_location_id']
            pcat_id = result['p_category_id']
            sql = """SELECT * FROM `product_location` WHERE `id`=%s"""
            cursor.execute(sql,ploc_id)
            result = cursor.fetchone()
            location = ProductLocations.from_dict(result)
            sql="""SELECT * FROM `product_category` WHERE `id`=%s"""
            cursor.execute(sql,pcat_id)
            result=cursor.fetchone()
            category = ProductCategories.from_dict(result)
            sql="""SELECT * FROM `product_list` WHERE `p_uid`=%s"""
            cursor.execute(sql,(p_uid))
            result = cursor.fetchone()

            product_list = ProductLists.from_dict(result)
            lr.append(ProductApiResponse(p_uid=p_uid,location=location,category=category,product_list=product_list)
)
    return lr
def patch_product(product:ProductApiResponse,order_id:str)->None:
    pass
def post_product(product:ProductApiResponse) -> ProductApiResponse:
    return "hi"
def add_customer(customer : Customers) -> None:
    with connection.cursor() as cursor:
        cusid = getcusid_fromemail(customer.emailid)
        
        if cusid is not None:
           raise NameError 
        query = "INSERT INTO customer (google_id, facebook_id, username, email, password, phone) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (customer.googleid,customer.facebookid, customer.username, customer.emailid, customer.password, customer.phone_number)
        cursor.execute(query, values)
        connection.commit()
        customer.cus_id=str(cursor.lastrowid)
def addotp(otp:str,email : str) -> None:
    """adds otp to cutomer with given email"""
    with connection.cursor() as cursor:
        sql = """UPDATE `customer` SET `otp`=%s WHERE `email`=%s"""
        cursor.execute(sql, (otp, email))
    connection.commit()
def getotp_frommail(email : str) -> str :
    with connection.cursor() as cursor:
        sql ="""SELECT `otp` FROM `customer` WHERE `email`=%s"""
        cursor.execute(sql,(email))
        result = cursor.fetchone()
        if result is None:
            return None
        otp = result["otp"]
        return otp
def get_passwd_frommail(email : str) -> None:

    pass
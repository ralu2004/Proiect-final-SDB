from domain.product import Product
from repository.repository import Repository


class AdminService:
    def __init__(self, product_repository: Repository):
        self.__product_repository = product_repository
        self.__product_list = self.__product_repository.get_all_entities()
        file = open("database", "r")
        for line in file:
            properties = line.split(",")
            self.__product_list.append(Product(properties[0], properties[1], properties[2], int(properties[3]),
                                               int(properties[4])))

    def add(self, barcode, name, quantity, company, price):
        """
        Given the arguments of a Product object, it ads it to the product list
        :param barcode: Product barcode
        :param name: Product name
        :param price: Product price
        :param quantity: Product quantity
        :param company: Product company
        :param promotion: Promotion, if exists
        :return:
        """
        self.__product_repository.add(Product(barcode, name, quantity, company, price))
        self.__update_database()

    def delete(self, barcode):
        """
        Given the barcode of a product, it deletes it from the product list
        :param barcode: Barcode of product to be deleted
        :return:
        """
        self.__product_repository.delete(Product(barcode, 0, 0, 0, 0))
        self.__update_database()

    def update_product(self, barcode, new_name, new_company, new_price, new_quantity):
        """
        Given the barcode of a product, the data related to it can be modified
        :param barcode: Product barcode
        :param new_name: The new name of the product
        :param new_price: The new price of the product
        :param new_company: The new company of the product
        :param new_quantity: The new quantity of a product
        :return:
        """
        for product in self.__product_list:
            if product.get_barcode() == barcode:
                product.set_name(new_name)
                product.set_company(new_company)
                product.set_price(new_price)
                product.set_quantity(new_quantity)

        self.__update_database()

    def print_product_list(self):
        """
        Returns the of all products
        :return: All existing products
        """
        return self.__product_repository.get_all_entities()

    def specific_products(self, company):
        """
        Return all products from a specific company
        :param company: The company of products to be returned
        :return: all products from given company
        """
        specific_products = []
        for product in self.__product_list:
            if product.get_company() == company:
                specific_products.append(product)
        return specific_products

    def __update_database(self):
        """
        Saves modifications in the product database
        :return:
        """
        file = open("database", "w")
        for product in self.__product_list:
            file.write(product.save())

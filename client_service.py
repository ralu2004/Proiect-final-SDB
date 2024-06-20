from repository.repository import Repository
from exceptions.exceptions import TooMuchException


class ClientService:
    def __init__(self, product_repository: Repository):
        self.__product_repository = product_repository
        self.__product_list = self.__product_repository.get_all_entities()

    def buy_product(self, name, company, quantity):
        """
        Given the name and company of a product, it can be bought in a specific quantity (if it is available)
        :param name: Name of product
        :param company: Company of product
        :param quantity: The specific quantity to be bought
        :return:
        """
        for product in self.__product_list:
            if product.get_name() == name and product.get_company() == company:
                if quantity > int(product.get_quantity()):
                    return TooMuchException
                else:
                    new_quantity = int(product.get_quantity()) - int(quantity)
                    product.set_quantity(new_quantity)
        self.__update_database()

    def print_product_list(self):
        """
        Returns the of all products
        :return: All existing products
        """
        return self.__product_repository.get_all_entities()

    def products_cheaper_than(self, price):
        """
        Return all products cheaper than the given price, in descending order
        :param price: The given price/ price to be compared with
        :return: All products cheaper than the given price
        """
        cheaper_products = []
        for product in self.__product_list:
            if product.get_price() < price:
                cheaper_products.append(product)
            cheaper_products.sort()
        return cheaper_products

    def __update_database(self):
        file = open("database", "w")
        for product in self.__product_list:
            file.write(product.save())


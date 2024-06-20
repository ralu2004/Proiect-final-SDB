class Product:
    def __init__(self, barcode, name, company, price, quantity):
        """
        Constructor for Product entity
        :param barcode: The barcode with which the product identifies (str)
        :param name: The name of the product (str)
        :param company: The company which produces the product (string)
        :param price: The price of the product (int)
        :param quantity: The quantity of the product (int)
        """
        self.__barcode = barcode
        self.__name = name
        self.__company = company
        self.__price = price
        self.__quantity = quantity

    def get_barcode(self):
        return self.__barcode

    def get_name(self):
        return self.__name

    def get_company(self):
        return self.__company

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_company(self, new_company):
        self.__company = new_company

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        self.__price = new_price

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def __eq__(self, other):
        return other.get_barcode() == self.__barcode

    def __repr__(self):
        return "Barcode: {0} name: {1}, company: {2}, price: {3}, quantity: {4} ".format(self.__barcode, self.__name,
                                                                                        self.__company, self.__price,
                                                                                        self.__quantity)

    def save(self):
        return "{0},{1},{2},{3},{4},\n".format(self.__barcode, self.__name,self.__company, self.__price, self.__quantity)

    def __lt__(self, other):
        return self.__price > other.__price


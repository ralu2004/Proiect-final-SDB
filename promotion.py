class Promotion:
    def __init__(self, value, barcodes):
        """
        Constructor for Promotion class
        :param value: The value of a promotion in percentages
        :param barcodes: Barcodes of a product in promotion
        """
        self.__value = value
        self.__barcodes = barcodes

    def get_value(self):
        return self.__value

    def get_barcodes(self):
        """
        Returns the barcodes of the products in promotion
        :return: Barcodes of the products in promotion
        """
        return self.__barcodes

    def __repr__(self):
        return "Promotion value: {0}, barcodes: {1}".format(self.__value, self.__barcodes)





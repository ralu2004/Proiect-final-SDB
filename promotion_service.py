from domain.promotion import Promotion
from domain.product import Product
from repository.repository import Repository


class PromotionService:
    def __init__(self, product_repository: Repository, promotion_repository: Repository):
        self.__product_repository = product_repository
        self.__promotion_repository = promotion_repository
        self.__promotion_list = self.__promotion_repository.get_all_entities()
        self.__product_list = self.__product_repository.get_all_entities()

    def __is_in_other_promotion(self, barcodes):
        """
        Verifies if the products we want to add in a new promotion already exist in another one, if so, they are deleted
        from the old one
        :param barcodes: Barcodes of products to be added in the new promotion
        :return:
        """
        for promotion in self.__promotion_list:
            if promotion.get_barcodes().intersection(barcodes) is not None:
                set = promotion.get_barcodes().intersection(barcodes)
                for barcode in set:
                    promotion.get_barcodes().remove(barcode)

    def add_promotion(self, value, barcodes):
        """
        Adds a new promotion
        :param value: The value of the promotion in percentages
        :param barcodes: Set of barcodes corresponding to the products added in the promotion
        :return:
        """
        self.__is_in_other_promotion(barcodes)
        self.__promotion_repository.add(Promotion(value, barcodes))

    def find_products_in_promotion(self):
        """
        Returns the products in promotions sorted by promotion value and price in descending order
        :return: Products in promotion
        """
        promotion_dict = {}

        for promotion in self.__promotion_list:
            for barcode in promotion.get_barcodes():
                for product in self.__product_list:
                    if barcode == product.get_barcode():
                        if promotion.get_value() not in promotion_dict.keys():
                            promotion_dict[promotion.get_value()] = [product]
                        else:
                            promotion_dict[promotion.get_value()].append(product)
        ordered_promotion_dict = {}
        for key in sorted(promotion_dict, reverse=True):
            promotion_dict[key].sort()
            ordered_promotion_dict[key] = promotion_dict[key]
        return ordered_promotion_dict

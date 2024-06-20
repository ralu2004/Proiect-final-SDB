from exceptions.exceptions import ProgramError
from service.client_service import ClientService
from service.admin_service import AdminService
from service.promotion_service import PromotionService
from validator.product_validator import ProductValidator


class Console:
    def __init__(self, client_service: ClientService, admin_service: AdminService, promotion_service: PromotionService,
                 product_validator: ProductValidator):
        self.__client_service = client_service
        self.__admin_service = admin_service
        self.__promotion_service = promotion_service
        self.__product_validator = product_validator

    def __print_main_menu(self):
        print("****** MAIN MENU ******")
        print("1.Admin menu")
        print("2.Client menu")
        print("0.Exit")

    def __print_admin_menu(self):
        print("****** ADMIN MENU ******")
        print("1.Add product")
        print("2.Delete product")
        print("3.Update product")
        print("4.Print product list")
        print("5.Print products from company: ")
        print("6.Add promotion")
        print("0.Back")

    def __print_client_menu(self):
        print("****** CLIENT MENU ******")
        print("1.Buy product")
        print("2.Print product list")
        print("3.Print products cheaper than: ")
        print("4.Print products in promotion")
        print("0.Back")

    def __add_product(self):
        """
        Adds a product
        :return:
        """
        barcode = input("Enter barcode: ")
        name = input("Enter name: ")
        company = input("Enter company: ")
        price = input("Enter price: ")
        self.__product_validator.validate_price(price)
        quantity = input("Enter quantity: ")
        self.__product_validator.validate_quantity(quantity)
        self.__admin_service.add(barcode, name, company, price, quantity)


    def __delete_product(self):
        """
        Deletes a product
        :return:
        """
        barcode = input("Enter the barcode of the product you want to delete: ")
        self.__admin_service.delete(barcode)

    def __update_product(self):
        """
        Allows the user to update product data
        :return:
        """
        barcode = input("Enter the barcode of the product you want to update: ")
        name = input("Enter the new name: ")
        company = input("Enter the new company: ")
        price = input("Enter the new price: ")
        quantity = input("Enter the new quantity: ")
        self.__admin_service.update_product(barcode, name, company, price, quantity)

    def __print_product_list(self):
        """
        Prints the list of products
        :return:
        """
        print("******Product List******")
        for product in self.__admin_service.print_product_list():
            print(product)

    def __print_specific_products(self):
        """
        Prints all products from a specific company
        :return:
        """
        company = str(input("Give company: "))
        print(self.__admin_service.specific_products(company))

    def __add_promotion(self):
        """
        Adds a new promotion
        :return:
        """
        value = input("Enter value(%): ")
        barcodes = set(input("Enter barcodes (with space between): ").split(" "))
        print("Products with barcodes: ", barcodes, "have been added in the new promotion")
        self.__promotion_service.add_promotion(value, barcodes)

    def __buy_product(self):
        """
        Allows the client to buy a product
        :return:
        """
        name = input("Enter the name of the product you want to buy: ")
        company = input("Enter the company of the product you want to buy: ")
        quantity = int(input("Enter the quantity: "))
        self.__client_service.buy_product(name, company, quantity)

    def __print_products_cheaper_than(self):
        """
        Prints all products which are cheaper than a given price
        :return:
        """
        price = int(input("Enter price: "))
        print("****** Cheaper Products ******")
        print(self.__client_service.products_cheaper_than(price))

    def __print_products_in_promotion(self):
        """
        Prints the products in promotion sorted by promotion value and price in descending order
        :return:
        """
        promotion_dict = self.__promotion_service.find_products_in_promotion()
        for key in promotion_dict.keys():
            for product in promotion_dict[key]:
                new_price = product.get_price() * (100 - int(key)) / 100
                print("Promotion value: ", key, product, " NEW PRICE: ", new_price)

    def run(self):
        while True:
            self.__print_main_menu()

            try:
                command = int(input("Choose command: "))
                if command == 0:
                    break
                elif command == 1:
                    self.__print_admin_menu()

                    command = int(input("Choose command: "))
                    if command == 0:
                        continue
                    elif command == 1:
                        self.__add_product()
                    elif command == 2:
                        self.__delete_product()
                    elif command == 3:
                        self.__update_product()
                    elif command == 4:
                        self.__print_product_list()
                    elif command == 5:
                        self.__print_specific_products()
                    elif command == 6:
                        self.__add_promotion()

                elif command == 2:
                    self.__print_client_menu()

                    command = int(input("Choose command: "))
                    if command == 0:
                        continue
                    elif command == 1:
                        self.__buy_product()
                    elif command == 2:
                        self.__print_product_list()
                    elif command == 3:
                        self.__print_products_cheaper_than()
                    elif command == 4:
                        self.__print_products_in_promotion()
            except ProgramError as error:
                print(error)

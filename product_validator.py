from exceptions.exceptions import ValidationError


class ProductValidator:
    def __init__(self) -> None:
        super().__init__()

    def validate_price(self, price):
        try:
            int_price = int(price)
        except Exception:
            raise ValidationError("Price of the product is not a number!")

    def validate_quantity(self, quantity):
        try:
            int_quantity = int(quantity)
        except Exception:
            raise ValidationError("Quantity of the product is not a number!")
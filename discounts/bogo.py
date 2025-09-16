
from discounts.base import DiscountBase

class BogoDiscount(DiscountBase):

    def __init__(self, **kwargs):

        try:
            self.__sku = kwargs["sku"]
            self.__required_quantity = kwargs["required_quantity"]
            self.__free_quantity = kwargs["free_quantity"]
        except KeyError as e:
            raise ValueError(f"Missing key in BogoDiscount data: {e}")

        super().__init__(**kwargs)

    def apply_discount(self):
        pass

    def __str__(self):
        return f"""
        Discount type: Bogo
        Items:
            -> SKU: {self.__sku}
            -> Required Quantity: {self.__required_quantity}
            -> Free Quantity: {self.__free_quantity}
        """
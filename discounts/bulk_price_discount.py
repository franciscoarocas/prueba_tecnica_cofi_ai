

from discounts.base import DiscountBase


class BulkPriceDiscount(DiscountBase):

    def __init__(self, **kwargs):

        try:
            self.__sku = kwargs["sku"]
            self.__min_quantity = kwargs["min_quantity"]
            self.__new_price = kwargs["new_price"]
        except KeyError as e:
            raise ValueError(f"Missing key in BulkPriceDiscount data: {e}")

        super().__init__(**kwargs)

    def apply_discount(self):
        pass

    def __str__(self):
        return f"""
        Discount type: Bulk Price
        Items:
            -> SKU: {self.__sku}
            -> Minimum Quantity: {self.__min_quantity}
            -> New Price: {self.__new_price}
        """


from discounts.base import DiscountBase


class BulkPriceDiscount(DiscountBase):
    """
        Bulk Price Discount Class
        If a customer buys a certain quantity of a specific product, the price per unit for that product is reduced.
        Attributes:
            sku (str): The SKU of the product to which the discount applies
            min_quantity (int): The minimum quantity required to trigger the discount
            new_price (Decimal): The new price per unit when the discount is applied
    """

    def __init__(self, **kwargs):
        """
            Initialize BulkPriceDiscount with sku, min_quantity, and new_price
            Args:
                **kwargs: Arbitrary keyword arguments containing sku, min_quantity, and new_price
            Raises:
                ValueError: If any of the required keys are missing in kwargs
        """

        try:
            self.__sku = kwargs["sku"]
            self.__min_quantity = kwargs["min_quantity"]
            self.__new_price = kwargs["new_price"]
        except KeyError as e:
            raise ValueError(f"Missing key in BulkPriceDiscount data: {e}")

        super().__init__(**kwargs)

    def apply_discount(self):
        pass

    def __str__(self) -> str:
        return f"""
        Discount type: Bulk Price
        Items:
            -> SKU: {self.__sku}
            -> Minimum Quantity: {self.__min_quantity}
            -> New Price: {self.__new_price}
        """
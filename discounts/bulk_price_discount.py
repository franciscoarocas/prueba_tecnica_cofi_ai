
from typing import List

from discounts.base import DiscountBase
from models.product import ProductType

from decimal import Decimal



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


    def apply_discount(self, products : List[ProductType]) -> Decimal:
        """
            Apply the bulk price discount to the list of products in the cart
            Args:
                products (List[ProductType]): The list of products in the cart
            Returns:
                Decimal: The total discount amount applied to the cart
        """

        total = Decimal('0.00')

        same_products = [product for product in products if product.code == self.__sku]

        if not same_products:
            return total

        if len(same_products) >= self.__min_quantity:
            for _ in range(len(same_products)):
                total += (same_products[0].price - self.__new_price)

        return total


    def __str__(self) -> str:
        return f"""
        Discount type: Bulk Price
        Items:
            -> SKU: {self.__sku}
            -> Minimum Quantity: {self.__min_quantity}
            -> New Price: {self.__new_price}
        """
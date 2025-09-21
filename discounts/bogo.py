
from discounts.base import DiscountBase

from typing import List
from models.product import ProductType

from decimal import Decimal



class BogoDiscount(DiscountBase):
    """
        Discount of type "Buy One Get One" (BOGO)
        E.g., Buy 1 get 1 free, Buy 2 get 1 free, etc.
    """

    def __init__(self, **kwargs):
        """
            Initialize BogoDiscount with required parameters.
            Args:
                sku (str): The SKU of the product to which the discount applies.
                required_quantity (int): The quantity that must be purchased to qualify for the free items.
                free_quantity (int): The quantity of free items given when the required quantity is purchased.
            Raises:
                ValueError: If any of the required keys are missing in kwargs.
        """

        try:
            self.__sku = kwargs["sku"]
            self.__required_quantity = kwargs["required_quantity"]
            self.__free_quantity = kwargs["free_quantity"]
        except KeyError as e:
            raise ValueError(f"Missing key in BogoDiscount data: {e}")

        super().__init__(**kwargs)


    def apply_discount(self, products : List[ProductType]) -> Decimal:
        """
            Apply the BOGO discount to the list of products.
            Args:
                products (List[ProductType]): The list of products in the cart.
            Returns:
                Decimal: The total discount applied.
        """

        bogo_products = [product for product in products if product.code == self.__sku]

        if not bogo_products:
            return Decimal('0.00')

        total_products_counts = len(bogo_products) // self.__required_quantity
        total_free_products = total_products_counts * self.__free_quantity

        total_discount = total_free_products * bogo_products[0].price

        return total_discount


    def __str__(self) -> str:
        return f"""
        Discount type: Bogo
        Items:
            -> SKU: {self.__sku}
            -> Required Quantity: {self.__required_quantity}
            -> Free Quantity: {self.__free_quantity}
        """

from typing import List

from discounts.base import DiscountBase
from models.product import ProductType

from decimal import Decimal


class BundleFixedPriceDiscount(DiscountBase):
    """
        Represents a bundle fixed price discount.
        A bundle fixed price discount allows customers to purchase a set of products at a fixed total price.
        Attributes:
            components (List[str]): List of product codes that are part of the bundle.
            bundle_price (Decimal): The fixed price for the bundle.
    """

    def __init__(self, **kwargs):
        """
            Creates a BundleFixedPriceDiscount instance.
            Components contains the list of product codes that are part of the bundle.
            Bundle_price is the fixed price for the bundle.
            Args:
                **kwargs: Arbitrary keyword arguments containing 'components' and 'bundle_price'.
            Raises:
                ValueError: If 'components' or 'bundle_price' are missing in kwargs.
        """

        try:
            self.__components = kwargs["components"]
            self.__bundle_price = Decimal(kwargs["bundle_price"])
        except KeyError:
            raise ValueError("Missing 'components' key in discount data")

        super().__init__(**kwargs)


    def apply_discount(self, products : List[ProductType]) -> Decimal:
        """
            Applies the bundle fixed price discount to the given list of products.
            Args:
                products (List[ProductType]): The list of products to which the discount will be applied.
            Returns:
                Decimal: The total discount amount.
        """

        counter_components = {component:0 for component in self.__components}
        products_prices = {component:0 for component in self.__components}

        for product in products:
            if product.code in counter_components:
                counter_components[product.code] += 1
                products_prices[product.code] = product.price

        min_count = min(counter_components.values())

        combo_price_without_discount = Decimal('0.00')

        for component in products_prices.values():
            combo_price_without_discount += component

        combo_without_discount = abs(combo_price_without_discount - self.__bundle_price)

        return combo_without_discount * min_count


    def __str__(self) -> str:
        return f"""
        Discount type: Bundle Fixed Price
        Items:
            -> Components: {self.__components}
            -> Bundle Price: {self.__bundle_price}
        """
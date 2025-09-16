
from discounts.base import DiscountBase


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
            self.__bundle_price = kwargs["bundle_price"]
        except KeyError:
            raise ValueError("Missing 'components' key in discount data")

        super().__init__(**kwargs)

    def apply_discount(self):
        pass

    def __str__(self) -> str:
        return f"""
        Discount type: Bundle Fixed Price
        Items:
            -> Components: {self.__components}
            -> Bundle Price: {self.__bundle_price}
        """
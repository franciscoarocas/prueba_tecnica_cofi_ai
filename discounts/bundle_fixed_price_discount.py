
from discounts.base import DiscountBase


class BundleFixedPriceDiscount(DiscountBase):

    def __init__(self, **kwargs):

        try:
            self.__components = kwargs["components"]
            self.__bundle_price = kwargs["bundle_price"]
        except KeyError:
            raise ValueError("Missing 'components' key in discount data")

        super().__init__(**kwargs)

    def apply_discount(self):
        pass

    def __str__(self):
        return f"""
        Discount type: Bundle Fixed Price
        Items:
            -> Components: {self.__components}
            -> Bundle Price: {self.__bundle_price}
        """
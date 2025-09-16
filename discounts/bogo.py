
from discounts.base import DiscountBase

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

    def apply_discount(self):
        pass

    def __str__(self) -> str:
        return f"""
        Discount type: Bogo
        Items:
            -> SKU: {self.__sku}
            -> Required Quantity: {self.__required_quantity}
            -> Free Quantity: {self.__free_quantity}
        """
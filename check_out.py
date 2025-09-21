
import logging

from typing import List

from models.product import ProductType
from models.discounts import DiscountType

from copy import copy

from decimal import Decimal

logger = logging.getLogger(__name__)



class CheckOut:
  """
    Class that represents a checkout system
    Attributes:
        discounts (List[DiscountType]): A list of discounts available
  """

  def __init__(self, discounts : List[DiscountType], **kwargs) -> None:
    """
      Initialize the checkout system with a list of discounts
      Args:
          discounts (List[DiscountType]): A list of discounts available
    """
    self.__discounts = {str(discount):discount for discount in discounts}
    self.__cart = []
    self.__debug = kwargs.get('debug', False)


  def scan(self, product : ProductType) -> ProductType:
    """
      Add a product to the cart
      Args:
          product (ProductType): The product to add to the cart
      Returns:
          ProductType: The product added to the cart
    """
    if self.__debug:
      logger.debug(f"Scanning product: {product.name} - Price: {product.price}")
    self.__cart.append(copy(product))
    return product


  def apply_discounts(self) -> Decimal:
    """
      Apply all discounts to the current cart and return the total discount amount.
      Returns:
          Decimal: The total discount amount applied to the cart
    """

    total = Decimal('0.00')

    for discount in self.__discounts.values():
      if self.__debug:
        logger.debug(f"Applying discount: {discount.id}")
      current_discount = discount.apply_discount(self.__cart)
      if self.__debug:
        logger.debug(f"Discount applied: {current_discount}")
      total += current_discount

    if self.__debug:
      logger.debug(f"Total discount applied: {total}")

    return total


  def total(self) -> Decimal:
    """
      Calculate the total price of the products in the cart, applying any discounts
      Returns:
          Decimal: The total price of the products in the cart
    """
    total = Decimal('0.00')
    for product in self.__cart:
      total += product.price

    total = total - self.apply_discounts()
    return total


  def print_products(self) -> None:
    """
      Print the products in the cart
    """

    product_counter = {}

    for product in self.__cart:

      name = product.name

      if name not in product_counter:
        product_counter[name] = 0

      product_counter[name] += 1

    for name, quantity in product_counter.items():
      print(f"Product Name: {name} - Product Quantity: {quantity}")

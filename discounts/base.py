
from abc import ABC, abstractmethod

from typing import Any

from decimal import Decimal



class DiscountBase(ABC):
    """
      Base class for all discount types
    """

    def __init__(self, **kwargs):
      """
        Initialize the discount with the given parameters.
        Save the ID of the discount.
        Args:
            **kwargs: Arbitrary keyword arguments containing discount parameters
        Raises:
            ValueError: If required keys are missing in kwargs
      """

      try:
        self.id = kwargs["id"]
      except KeyError:
        raise ValueError("Missing 'id' key in discount data")

    @abstractmethod
    def apply_discount(self, items : Any) -> Decimal:
      pass

    @abstractmethod
    def __str__(self) -> str:
      pass
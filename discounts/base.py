
from abc import ABC, abstractmethod

from typing import Any

from decimal import Decimal



class DiscountBase(ABC):

    def __init__(self, **kwargs):

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
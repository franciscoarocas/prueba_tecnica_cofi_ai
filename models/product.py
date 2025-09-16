
from dataclasses import dataclass

from decimal import Decimal
from typing import List, TypedDict


@dataclass
class ProductType:
  code  : str
  name  : str
  price : Decimal

  def __post_init__(self):
    if self.price < 0:
      raise ValueError("El precio no puede ser inferior a 0")


class ProductJsonItemType(TypedDict):
  code   : str
  name   : str
  price  : float

ProductJsonType = List[ProductJsonItemType]
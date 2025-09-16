
from decimal import Decimal
from typing import List

from models.product import ProductJsonType, ProductType

import json

import logging

logger = logging.getLogger(__name__)



def load_json_data(json_data: str) -> ProductJsonType:
  """
    Open a JSON string which contains the data of all products
    Args:
        json_data (str): JSON string representing a list of products
    Returns:
        ProductJsonType: A list of products represented as dictionaries
  """
  try:
    items = json.loads(json_data)
  except json.JSONDecodeError as e:
    logger.error("Failed to decode JSON data")
    raise ValueError("Invalid JSON data") from e

  return items




def products_loader(json_data : ProductJsonType) -> List[ProductType]:
  """
    Recibe an a list of products in JSON format and returns a list of ProductType instances
    Args:
        json_data (ProductJsonType): A list of products represented as dictionaries
    Returns:
        List[ProductType]: A list of ProductType instances
  """

  result = []

  for product in json_data:

    try:
      result.append(ProductType(
        code  = product['code'],
        name  = product['name'],
        price = Decimal(product['price'])
      ))
    except KeyError as e:
      logger.error(f"Missing key in product data: {e}")
      raise ValueError(f"Missing key in product data: {e}")
    except (Decimal.InvalidOperation, TypeError) as e:
      logger.error(f"Invalid price value: {product.get('price')}")
      raise ValueError(f"Invalid price value: {product.get('price')}")
    except ValueError as e:
      logger.error(f"Error creating ProductType: {e}")
      raise e

  return result



def print_products(products: List[ProductType]) -> None:
  """
    Print the list of products in a readable format
    Args:
        products (List[ProductType]): A list of ProductType instances
    Returns:
        None
  """
  for product in products:
    print(f"Code: {product.code}, Name: {product.name}, Price: {product.price}")
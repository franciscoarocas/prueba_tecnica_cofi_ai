
import json
import logging

from typing import List

from discounts.base import DiscountBase
from discounts.bogo import BogoDiscount
from discounts.bundle_fixed_price_discount import BundleFixedPriceDiscount
from discounts.bulk_price_discount import BulkPriceDiscount

from models.discounts import discount_json_item


logger = logging.getLogger(__name__)


def load_discounts(discount_json_path : str) -> discount_json_item:
  """
    Load discounts from a JSON file.
    Args:
        discount_json_path (str): The path to the JSON file containing discount data.
    Returns:
        discount_json_item: A list of discounts represented as dictionaries.
  """

  try:
    with open(discount_json_path, 'r', encoding='utf-8') as f:
        discounts = json.load(f)
  except FileNotFoundError as e:
    logger.error(f"File not found: {discount_json_path}")
    raise e
  except json.JSONDecodeError as e:
    logger.error(f"Error decoding JSON from file: {discount_json_path}")
    raise e

  return discounts


FACTORY_ITEMS_MAP = {
  "BOGO"               : BogoDiscount,
  "BUNDLE_FIXED_PRICE" : BundleFixedPriceDiscount,
  "BULK_PRICE"         : BulkPriceDiscount
}


def discount_factory(discount_items : discount_json_item) -> List[DiscountBase]:
  """
    Create discount instances from a list of discount data.
    Args:
        discount_items (discount_json_item): A list of discount items represented as dictionaries.
    Returns:
        List[DiscountBase]: A list of instantiated discount objects.
  """

  result = []

  for item in discount_items:
    item_type = item.get("type")

    discount_class = FACTORY_ITEMS_MAP.get(item_type)
    if not discount_class:
      raise KeyError(f"Discount type '{item_type}' not found in FACTORY_ITEMS_MAP")

    result.append(discount_class(**item))

  return result



def print_all_discounts(discounts : List[DiscountBase]) -> None:
  """
    Print all discounts in a readable format
    Args:
        discounts (List[DiscountBase]): A list of DiscountBase instances
    Returns:
        None
  """
  for discount in discounts:
    print(discount)
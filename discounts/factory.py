
import json

from discounts.bogo import BogoDiscount
from discounts.bundle_fixed_price_discount import BundleFixedPriceDiscount
from discounts.bulk_price_discount import BulkPriceDiscount


def load_discounts(discount_json_path : str):

  try:
    with open(discount_json_path, 'r', encoding='utf-8') as f:
        discounts = json.load(f)
  except FileNotFoundError:
    print(f"File not found: {discount_json_path}")
  except json.JSONDecodeError:
    print(f"Error decoding JSON from file: {discount_json_path}")

  return discounts


FACTORY_ITEMS_MAP = {
  "BOGO"               : BogoDiscount,
  "BUNDLE_FIXED_PRICE" : BundleFixedPriceDiscount,
  "BULK_PRICE"         : BulkPriceDiscount
}


def discount_factory(discount_items):

  result = []

  for item in discount_items:
    item_type = item.get("type")

    discount_class = FACTORY_ITEMS_MAP.get(item_type)
    if not discount_class:
      raise KeyError(f"Discount type '{item_type}' not found in FACTORY_ITEMS_MAP")

    result.append(discount_class(**item))

  return result



def print_all_discounts(discounts) -> None:
  for discount in discounts:
    print(discount)
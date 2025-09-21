
from typing import Dict, Any, TypedDict

discount_json_item = Dict[str, Any]


class DiscountType(TypedDict):
    id : str


class BogoDiscountType(TypedDict):
    type: str
    buy: str
    get: str


class BulkDiscountType(TypedDict):
    type: str
    sku: str
    min_quantity: int
    new_price: str


class BundleFixedPriceDiscountType(TypedDict):
    type: str
    skus: list[str]
    bundle_price: str
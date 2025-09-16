
from typing import Dict, Any, TypedDict

discount_json_item = Dict[str, Any]



class BogoDiscountType(TypedDict):
    type: str
    buy: str
    get: str
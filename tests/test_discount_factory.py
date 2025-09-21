
import pytest
import tempfile
import json

from discounts.factory import discount_factory
from discounts.base import DiscountBase
from discounts.factory import load_discounts

def test_load_discounts_valid():
    data = [
        {"id": "d1", "type": "BOGO", "sku": "A", "required_quantity": 2, "free_quantity": 1},
        {"id": "d2", "type": "BULK_PRICE", "sku": "B", "min_quantity": 3, "new_price": 8.00}
    ]
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
        json.dump(data, tmp)
        tmp.flush()
    result = load_discounts(tmp.name)
    assert result == data

def test_load_discounts_file_not_found():
    fake_path = 'doesnt_exist_12345.json'
    with pytest.raises(FileNotFoundError):
        load_discounts(fake_path)

def test_load_discounts_json_decode_error(tmp_path):
    file_path = tmp_path / 'invalid.json'
    file_path.write_text('esto no es un json válido', encoding='utf-8')
    with pytest.raises(ValueError):
        load_discounts(str(file_path))


def test_discount_factory_valid():
    items = [
        {"id": "d1", "type": "BOGO", "sku": "A", "required_quantity": 2, "free_quantity": 1},
        {"id": "d2", "type": "BULK_PRICE", "sku": "B", "min_quantity": 3, "new_price": 8.00}
    ]
    discounts = discount_factory(items)
    assert len(discounts) == 2
    assert isinstance(discounts[0], DiscountBase)
    assert discounts[0].id == "d1"
    assert discounts[1].id == "d2"

def test_discount_factory_invalid_type():
    items = [
        {"id": "d3", "type": "UNKNOWN", "sku": "C"}
    ]
    with pytest.raises(KeyError) as excinfo:
        discount_factory(items)
    assert "Discount type 'UNKNOWN' not found in FACTORY_ITEMS_MAP" in str(excinfo.value)

def test_discount_factory_missing_required_param():
    items = [
        {"type": "BOGO", "sku": "A", "required_quantity": 2, "free_quantity": 1}  # falta id
    ]
    with pytest.raises(ValueError) as excinfo:
        discount_factory(items)
    assert "Missing 'id' key in discount data" in str(excinfo.value)

def test_print_all_discounts(capsys):
    from discounts.factory import print_all_discounts
    from discounts.bogo import BogoDiscount
    discounts = [
        BogoDiscount(id="d1", sku="A", required_quantity=2, free_quantity=1)
    ]
    print_all_discounts(discounts)
    captured = capsys.readouterr()
    assert "Discount type: Bogo" in captured.out
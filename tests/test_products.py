

import tempfile
import json
import pytest

from product import products_loader, load_json_data, print_products, ProductType

from decimal import Decimal


def test_load_json_data_valid():

    data = [
        {"code": "VOUCHER", "name": "Cofi Voucher", "price": 5.00},
        {"code": "TSHIRT", "name": "Cofi T-Shirt", "price": 20.00}
    ]

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
        json.dump(data, tmp)
        tmp.flush()
    result = load_json_data(tmp.name)
    assert result == data


def test_load_json_data_file_not_found():

    fake_path = 'doesnt_exist_12345.json'
    with pytest.raises(FileNotFoundError):
        load_json_data(fake_path)


def test_load_json_data_json_decode_error(tmp_path):
    file_path = tmp_path / 'invalid.json'
    file_path.write_text('esto no es un json válido', encoding='utf-8')
    with pytest.raises(ValueError) as excinfo:
        load_json_data(str(file_path))
    assert "Invalid JSON data" in str(excinfo.value)


def test_products_loader_value_error():
    json_data = [
        {"code": "P001", "name": "Product 1", "price": "no_es_decimal"}
    ]

    with pytest.raises(ValueError) as excinfo:
        products_loader(json_data)
    assert "Invalid price value" in str(excinfo.value)


def test_products_loader_valid_data():
    json_data = [
        {"code": "P001", "name": "Product 1", "price": "10.50"},
        {"code": "P002", "name": "Product 2", "price": "20.00"}
    ]
    products = products_loader(json_data)
    assert len(products) == 2
    assert products[0].code == "P001"
    assert products[0].name == "Product 1"
    assert products[0].price == Decimal('10.50')
    assert products[1].code == "P002"
    assert products[1].name == "Product 2"
    assert products[1].price == Decimal('20.00')


def test_products_loader_missing_key():
    json_data = [
        {"code": "P001", "name": "Product 1"},
    ]
    with pytest.raises(ValueError) as excinfo:
        products_loader(json_data)
    assert "Missing key in product data" in str(excinfo.value)


def test_products_loader_invalid_price():
    json_data = [
        {"code": "P001", "name": "Product 1", "price": "invalid_price"},
    ]
    with pytest.raises(ValueError) as excinfo:
        products_loader(json_data)
    assert "Invalid price value" in str(excinfo.value)


def test_producttype_post_init_negative_price():
    with pytest.raises(ValueError) as excinfo:
        ProductType(code="X", name="Producto X", price=Decimal("-1.00"))
    assert "El precio no puede ser inferior a 0" in str(excinfo.value)


def test_print_products(capsys):

    products = [
        ProductType(code="A", name="Producto A", price=Decimal("10.00")),
        ProductType(code="B", name="Producto B", price=Decimal("20.00"))
    ]
    print_products(products)
    captured = capsys.readouterr()
    assert "Code: A, Name: Producto A, Price: 10.00" in captured.out
    assert "Code: B, Name: Producto B, Price: 20.00" in captured.out
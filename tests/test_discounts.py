
import pytest

from discounts.base import DiscountBase
from discounts.bogo import BogoDiscount
from discounts.bulk_price_discount import BulkPriceDiscount
from discounts.bundle_fixed_price_discount import BundleFixedPriceDiscount

from models.product import ProductType
from decimal import Decimal



def test_discountbase_cannot_instantiate():
    with pytest.raises(TypeError):
        DiscountBase(id="test")


def test_discountbase_missing_id():
    class DummyDiscount(DiscountBase):
        def apply_discount(self, items):
            return 0
        def __str__(self):
            return "dummy"
    with pytest.raises(ValueError):
        DummyDiscount()


def test_bogo_discount_applies_correctly():
    discount = BogoDiscount(id="d1", sku="A", required_quantity=2, free_quantity=1)
    products = [
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
    ]
    # 3 productos, por cada 2 compras, 1 gratis (solo 1 vez)
    assert discount.apply_discount(products) == Decimal("10.00")


def test_bogo_discount_missing_param():
    with pytest.raises(ValueError):
        BogoDiscount(id="d1", required_quantity=2, free_quantity=1)  # falta sku


def test_bogo_discount_no_products():
    discount = BogoDiscount(id="d1", sku="A", required_quantity=2, free_quantity=1)
    products = [
        ProductType(code="B", name="ProdB", price=Decimal("10.00")),
    ]
    assert discount.apply_discount(products) == Decimal("0.00")



def test_bogo_discount_str():
    discount = BogoDiscount(id="d1", sku="A", required_quantity=2, free_quantity=1)
    result = str(discount)
    assert "Discount type: Bogo" in result
    assert "SKU: A" in result
    assert "Required Quantity: 2" in result
    assert "Free Quantity: 1" in result



def test_bulk_price_discount_applies_correctly():
    discount = BulkPriceDiscount(id="d2", sku="A", min_quantity=3, new_price=Decimal("8.00"))
    products = [
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
    ]
    # 3 productos, precio original 10, nuevo precio 8, descuento total = 3 * (10-8) = 6
    assert discount.apply_discount(products) == Decimal("6.00")



def test_bulk_price_discount_not_applied_if_quantity_low():
    discount = BulkPriceDiscount(id="d2", sku="A", min_quantity=4, new_price=Decimal("8.00"))
    products = [
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
    ]
    # Solo hay 3 productos, min_quantity es 4, no se aplica descuento
    assert discount.apply_discount(products) == Decimal("0.00")



def test_bulk_price_discount_missing_param():
    with pytest.raises(ValueError):
        BulkPriceDiscount(id="d2", min_quantity=3, new_price=Decimal("8.00"))  # falta sku



def test_bulk_price_discount_str():
    discount = BulkPriceDiscount(id="d2", sku="A", min_quantity=3, new_price=Decimal("8.00"))
    result = str(discount)
    assert "Discount type: Bulk Price" in result
    assert "SKU: A" in result
    assert "Minimum Quantity: 3" in result
    assert "New Price: 8.00" in result



def test_bulk_price_discount_no_matching_products():
    discount = BulkPriceDiscount(id="d2", sku="A", min_quantity=3, new_price=Decimal("8.00"))
    products = [
        ProductType(code="B", name="ProdB", price=Decimal("10.00")),
        ProductType(code="C", name="ProdC", price=Decimal("12.00")),
    ]
    # Ningún producto tiene el SKU "A", así que el descuento debe ser 0
    assert discount.apply_discount(products) == Decimal("0.00")



def test_bundle_fixed_price_discount_applies_correctly():
    discount = BundleFixedPriceDiscount(id="d3", components=["A", "B"], bundle_price=Decimal("25.00"))
    products = [
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="B", name="ProdB", price=Decimal("20.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="B", name="ProdB", price=Decimal("20.00")),
    ]
    # Hay 2 combos posibles: (A+B) x2, precio sin descuento = 10+20=30, bundle=25, descuento por combo=5, total=10
    assert discount.apply_discount(products) == Decimal("10.00")



def test_bundle_fixed_price_discount_not_applied_if_missing_component():
    discount = BundleFixedPriceDiscount(id="d3", components=["A", "B"], bundle_price=Decimal("25.00"))
    products = [
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
        ProductType(code="A", name="ProdA", price=Decimal("10.00")),
    ]
    # Falta el producto B, no hay combo, descuento=0
    assert discount.apply_discount(products) == Decimal("0.00")



def test_bundle_fixed_price_discount_missing_param():
    with pytest.raises(ValueError):
        BundleFixedPriceDiscount(id="d3", bundle_price=Decimal("25.00"))  # falta components



def test_bundle_fixed_price_discount_str():
    discount = BundleFixedPriceDiscount(id="d3", components=["A", "B"], bundle_price=Decimal("25.00"))
    result = str(discount)
    assert "Discount type: Bundle Fixed Price" in result
    assert "Components: ['A', 'B']" in result
    assert "Bundle Price: 25.00" in result
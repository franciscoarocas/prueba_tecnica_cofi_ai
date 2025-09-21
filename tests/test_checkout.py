

from check_out import CheckOut
from models.product import ProductType
from decimal import Decimal

class DummyDiscount:
    def __init__(self, id, value):
        self.id = id
        self.value = Decimal(value)
    def apply_discount(self, cart):
        return self.value
    def __str__(self):
        return f"DummyDiscount-{self.id}"

def test_checkout_scan_and_total_without_discounts():
    checkout = CheckOut(discounts=[], debug=True)
    p1 = ProductType(code="A", name="ProdA", price=Decimal("10.00"))
    p2 = ProductType(code="B", name="ProdB", price=Decimal("20.00"))
    checkout.scan(p1)
    checkout.scan(p2)
    assert checkout.total() == Decimal("30.00")

def test_checkout_total_with_discount():
    discount = DummyDiscount(id="d1", value="5.00")
    checkout = CheckOut(discounts=[discount], debug=True)
    p1 = ProductType(code="A", name="ProdA", price=Decimal("10.00"))
    p2 = ProductType(code="B", name="ProdB", price=Decimal("20.00"))
    checkout.scan(p1)
    checkout.scan(p2)
    assert checkout.total() == Decimal("25.00")  # 30 - 5

def test_checkout_apply_discounts_multiple():
    d1 = DummyDiscount(id="d1", value="2.00")
    d2 = DummyDiscount(id="d2", value="3.00")
    checkout = CheckOut(discounts=[d1, d2], debug=True)
    p1 = ProductType(code="A", name="ProdA", price=Decimal("10.00"))
    checkout.scan(p1)
    assert checkout.apply_discounts() == Decimal("5.00")

def test_checkout_print_products(capsys):
    checkout = CheckOut(discounts=[], debug=True)
    p1 = ProductType(code="A", name="ProdA", price=Decimal("10.00"))
    p2 = ProductType(code="A", name="ProdA", price=Decimal("10.00"))
    p3 = ProductType(code="B", name="ProdB", price=Decimal("20.00"))
    checkout.scan(p1)
    checkout.scan(p2)
    checkout.scan(p3)
    checkout.print_products()
    captured = capsys.readouterr()
    assert "Product Name: ProdA - Product Quantity: 2" in captured.out
    assert "Product Name: ProdB - Product Quantity: 1" in captured.out
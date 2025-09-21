
from product import print_products, products_loader, load_json_data
from discounts.factory import load_discounts, discount_factory, print_all_discounts

from check_out import CheckOut


if __name__ == '__main__':

  products = products_loader(load_json_data('products.json'))
  print("Products loaded successfully:")
  print_products(products)

  discounts = discount_factory(load_discounts('discounts.json'))
  print("Discounts loaded successfully:")
  print_all_discounts(discounts)

  checkout = CheckOut(discounts, debug=True)

  checkout.scan(products[0])
  checkout.scan(products[1])

  print("Products in the cart:")
  checkout.print_products()
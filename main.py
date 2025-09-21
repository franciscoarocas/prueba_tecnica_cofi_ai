
from product import print_products, products_loader, load_json_data
from discounts.factory import load_discounts, discount_factory, print_all_discounts

from check_out import CheckOut


if __name__ == '__main__':

  products = products_loader(load_json_data('products.json'))
  products_dict = {product.code: product for product in products}
  print("Products loaded successfully:")
  print_products(products)

  discounts = discount_factory(load_discounts('discounts.json'))
  print("Discounts loaded successfully:")
  print_all_discounts(discounts)

  checkout = CheckOut(discounts, debug=True)

  checkout.scan(products_dict['VOUCHER'])
  checkout.scan(products_dict['VOUCHER'])
  checkout.scan(products_dict['VOUCHER'])
  checkout.scan(products_dict['TSHIRT'])
  checkout.scan(products_dict['MUG'])

  print("Products in the cart:")
  checkout.print_products()

  print(f"Total price: {checkout.total()}")
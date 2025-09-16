
from product import print_products, products_loader, load_json_data
from discounts.factory import load_discounts, discount_factory, print_all_discounts


if __name__ == '__main__':

  products = products_loader(load_json_data('products.json'))
  print("Products loaded successfully:")
  print_products(products)

  discounts = discount_factory(load_discounts('discounts.json'))
  print("Discounts loaded successfully:")
  print_all_discounts(discounts)

from product import print_products, products_loader, load_json_data


if __name__ == '__main__':

  with open('products.json', 'r', encoding='utf-8') as f:
    json_data = f.read()

  products = products_loader(load_json_data(json_data))
  print("Products loaded successfully:")
  print_products(products)
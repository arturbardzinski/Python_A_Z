

class Warehouse:

    def __init__ (self, product_list):
        self.product_list = product_list

    def show_products(self):
        print('This is all avalibles products: ')
        for product in self.product_list:
            print(product)

    def add_product(self):
        self.product_name = input('Type name of product: >>> ')
        if self.product_name not in self.product_list:
            self.product_list.append(self.product_name)
        print(f'Product {self.product_name} was added to warehouse.')

    def remove_product(self):
        self.product_name = input('Type name of product, to delete him: >>> ')
        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            print('You deleted product from warehouse.')
        else:
            print('This product do not exist in warehouse.')
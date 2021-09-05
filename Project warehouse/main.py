import sys
import time

class Warehouse:

    def __init__ (self, product_list):
        self.product_list = product_list

    def show_products(self):
        print('This is all avalibles products: ')
        for product in self.product_list:
            time.sleep(1)
            print(product)
            time.sleep(0.5)

    def add_product(self):
        self.product_name = input('Type name of product: >>> ')
        if self.product_name not in self.product_list:
            self.product_list.append(self.product_name)
        time.sleep(1)
        print(f'Product {self.product_name} was added to warehouse.')

    def remove_product(self):
        self.product_name = input('Type name of product, to delete him: >>> ')
        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            time.sleep(1)
            print('You deleted product from warehouse.')
        else:
            time.sleep(1)
            print('This product do not exist in warehouse.')

warehouse = Warehouse(['milk', 'eggs', 'water'])

while True:
    print('*' * 30)
    print('Type 1 to show products.')
    print('Type 2 to add products.')
    print('Type 3 to remove products.')
    print('Type 4 to close program.')
    print('*' * 30)
    user_choise = int(input('>>> '))

    if user_choise == 1:
        warehouse.show_products()
    elif user_choise == 2:
        warehouse.add_product()
    elif user_choise == 3:
        warehouse.remove_product()
    elif user_choise == 4:
        ending = '*** End of program ***'
        for letter in ending:
            sys.stdout.write(letter)
            time.sleep(0.05)
        sys.exit()
    else:
        print('Type 1, 2, 3 or 4')



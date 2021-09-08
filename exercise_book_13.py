

import math

class Shape():
  def what_i_am(self):
    print('Jestem figurą')

class Circle(Shape):
  def __init__ (self, radius):
    self.radius = radius

  def calculate_perimeter(self):
    return 2 * math.pi * self.radius

class Squere(Shape):
  def __init__ (self, side):
    self.side = side

  def calculate_perimeter(self):
    return 4* self.side
  
  def change_size(self, new_side):
    self.side += new_side

circle = Circle(5)
squere = Squere(3)

print(circle.calculate_perimeter())
print(squere.calculate_perimeter())

squere.change_size(5)
print(squere.calculate_perimeter())
print(circle.what_i_am())
print(squere.what_i_am())


class Owner():
  def __init__(self, name):
    self.name = name


class Horse(Owner):
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner

owner = Owner('Tadek')
horse = Horse('Konik', owner)

print(horse.owner.name)

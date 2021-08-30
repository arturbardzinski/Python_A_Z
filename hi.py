from date_test import date_now

print('This is my first program')
print('*' * 30)
print('Please enter your name: ')
name = input()
print('Hi, {}! Welcome to the system' .format(name))
print()
print('Please enter your year of birth: ')
year_b = int(input())
#teach how to use time in this

now = date_now()
year_now = now - int(year_b)
#print('{}, you have {} year old.'. format(name, year_now))


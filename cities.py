'''
Ćwiczenie 4
Podana jest lista miast:

cities = ['Warsaw', 'London', 'Berlin', 'New York']
Używając funkcji map() oraz wyrażenia lambda uzyskaj listę zawierającą trzy pierwsze litery każdego miasta.

Otrzymaną listę wydrukuj do konsoli.
'''
cities = ['Warsaw', 'London', 'Berlin', 'New York']

print(list(map(lambda word: word[:3], cities)))
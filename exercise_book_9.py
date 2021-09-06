

'''
with open('data.txt', 'r') as f:
  dataf = f.read()
print(dataf)

'''
# zada pytanie i zapisze odp w pliku

'''
print('Podaj mi swoje imię?')
answer = input('>>> ')

with open('name.txt', 'w+') as f:
  file = f.write(answer)
  
print('Zapisałeś do pliku >>> {}.'.format(answer))

with open('name.txt', 'r') as f:
  file = f.read()
  print('Zawartość pliku to: ')
  print(file)

'''

# zapisze w pliku CSV zawartość listy w liście.
# dane z każdej listy mają być zapisane w osobnych wierszach i rozdzielone przecinkami

import csv


movies = [['Top Gun', 'Oceans Eleven', 'Raport mniejszości'], ['Titanic', 'Ostatni Jedi', 'Incepcja']]

with open('movies.csv', 'w+') as f:
    writer = csv.writer(f, delimiter = ',')
    for movie_list in movies:
      writer.writerow(movie_list)

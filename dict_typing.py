import time
import sys
s = sys.stdout

print('*' *30)
print("Current date and time: ")
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print('*' *30)
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try:
  print(users[user_id])
except KeyError:  
  text = (f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza... \n\n')
  for l in text:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.07)
  
  users.setdefault(user_id, None)

print(users)
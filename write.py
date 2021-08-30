'''
Utwórz listę z podanych nazw technologii:

python
java
sql
sas
Następnie zapisz każdy element listy w nowej linii pliku techs.txt. '''

techs = ['python', 'java', 'sql', 'sas']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)

even_number = list(range(20))[::2]
print(even_number)

with open('techs.txt', 'a') as file:
    for number in even_number:
        print(number, file=file)

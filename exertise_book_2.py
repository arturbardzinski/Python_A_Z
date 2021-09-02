# 1. lista ulubionych muzyków

music = ['Mozart', 'Pink', 'Lady gaga']

print(type(music))

# 2. lista krotek miejsc i współrzędnych

my_vacation = [(34.255, 34, 888), (34.654, 123.456)]

# 3. słownik o mnie

me = {'imie': 'Artur',
    'wzrost': '171',
    'waga': '67',
    'oczy': 'niebieskie'
}

print(me)

# 4. Program, który pyta o moje dane

answer = input('''Czego chcesz się o mnie dowiedzieć:
                - imie
                - wzrost
                - waga
                - oczy
                ''')
print()

if answer in me:
    result = me[answer]  # result - zupełnie nowy
    print(result)
else:
    print('Brak danych')

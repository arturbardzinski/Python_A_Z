
"""
list1 = ['Noc żywych trupów', 'Pamiętnik wampirow', 'Ekipa']

for movie in list1:
    print(movie)


for i in range(25, 51):
    print(i) 


for (i, movie) in enumerate(list1):
    print(i, movie)
"""

'''
numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Odgadnij liczbę lub wpisz q, aby wyjść.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("wpisz liczbę lub naciśnij klawisz q, aby wyjść.")
    if answer in numbers:
        print("Udało ci się odgadnąć!")
    else:
        print("Nie udało ci się odgadnąć!")
        
'''
l1 = [8, 19, 148, 4]
l2 = [9, 1, 33, 83]
l3 =[]

for i in l1:
    for j in l2:
        l3.append(i * j)

print(l3)

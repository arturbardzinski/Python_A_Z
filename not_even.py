'''
Ćwiczenie 3
Napisz funkcję drukuj_nieparzyste, która zwróci listę liczb nieparzystych większych od zera i mniejszych od 20.



Oczekiwany rezultat: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Uwaga: Do oceny zadania wystarczy samo zdefiniowanie funkcji, nie trzeba jej wywoływać.
'''
x = 1

def not_even(maximum):
    result = []
    for i in range (maximum):
        if i % 2 == 1:
            result.append(i)
    return result

print(not_even(20))


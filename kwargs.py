'''
Ćwiczenie 6
Napisz funkcję policz_kwargs , która zwróci liczbę przekazanych tzw. 'keyword argument' (argumentów,
które podajemy przy pomocy nazwy zmiennej) podczas wywołania funkcji.



Przykład:

policz_kwargs(a=1, b=2, c=3) -> 3
policz_kwargs(10, a=1, b=2) -> 2
'''

def policz(*args, **kwargs):
    return len(kwargs)

print(policz(a=1, b=2, c=3))
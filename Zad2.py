def liczby(numbers):
    lista = []
    for number in numbers:
        lista.append(number*2)
    return lista

def liczby2(numbers):
    lista = [number*2 for number in numbers]
    return lista

lista2 = range(5)
print(liczby(lista2))
print(liczby2(lista2))

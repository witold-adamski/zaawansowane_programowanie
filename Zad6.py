def lists(lista1: list, lista2: list) -> list:
    lista3 = lista1 + lista2
    return list(set([n*n*n for n in lista3]))


lista1=[1, 5, 4]
lista2=[1, 2, 3]
print(lists(lista1, lista2))

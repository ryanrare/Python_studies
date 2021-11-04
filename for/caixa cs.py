lista1 = [int(x) for x in range(1000)]


def numeros_pares(lista: list) -> list:
    listaPares = list()
    for x  in lista:
        if x % 2 == 0:
            listaPares.append(x)
    return listaPares



print(numeros_pares(lista1))


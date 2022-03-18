from apoio_exercicio import pessoas

def filtrando(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtrando, pessoas)
for pessoa in nova_lista:
    print(pessoa)
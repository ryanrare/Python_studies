from apoio_exercicio import  pessoas, produtos, lista

new_list = map(lambda x: x * 2, lista )
print(list(new_list))
print('/'*50)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

produtos_aumentados = map(aumenta_preco, produtos)
for produto in produtos_aumentados:
    print(produto)
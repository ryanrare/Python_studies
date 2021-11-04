# exercicio 1
# def saudacao_nome(saudacao, nome):
#     print(f'{saudacao}, {nome}')
#
# saudacao_nome('ola', 'pedro')

# exercicio 2
# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
# soma(23, 43, 21)

# exercicio 3
# def aumento_percetual(valor, percetual):
#     return valor + (valor * percetual / 100)
#
# ap = aumento_percetual(23, 10)
# print(ap)

# exercicio 4
# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'fizzbuzz'
#     if n % 3 == 0:
#         return 'fizz'
#     if n % 5 == 0:
#         return 'buzz'
#     return n
#
# print(fizzbuzz(25))



# ////////
# def func(*args, **kwargs):
#     print(args)
#     idade = kwargs ['idade']
#     print(idade)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='ryan', sobrenome='victor', idade=19)




# exercicio2
# def ola_mundo():
#     return 'ola mundo'
#
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)


# # exer2/2
# def mestre(funcao, *args, **kwargs):
#     return funcao(*args, **kwargs)
#
# def fala_oi(nome):
#     return f'oi {nome}'
#
# def saudacao(nome, saudacao):
#     return f'{nome},{saudacao}'
#
# executando = mestre(fala_oi, 'ryan')
# executando2 = mestre(saudacao, 'ryan', saudacao='bom dia')
# print(executando)
# print(executando2)
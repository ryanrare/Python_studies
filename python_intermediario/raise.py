def divide(n1,  n2):
    if n2 == 0:
        raise ValueError('valor de n2 nao pode ser dividido.')
    return n1/n2
try:
    print(divide(n1= 2, n2=0))
except ValueError as error
    print("voce esta tentando dividir por 0")
    print('log:', error)
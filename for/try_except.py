try:
    a = 0
    try:
        a = 1/0
    except:
        print('erro')
except NameError as error:
    print('erro do desenvolvedor, fale com ele')
except (IndexError, KeyError):
    print('erro de indice ou chave')
except Exception as error:
    print('aconteceu um erro inesperado')
else:
    pass
finally:
    a = ''

print(a)
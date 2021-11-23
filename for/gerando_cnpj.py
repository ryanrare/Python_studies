import random
from validando_cnpj import calcula_digito, apenas_numeros

def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
        f'{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = calcula_digito(cnpj=inicio_cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)

    return novo_cnpj


def formata(cnpj):
    cnpj = apenas_numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
from itertools import groupby, tee

alunos = [
    {'nome': 'marcos', 'nota': 'D'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

def ordena(item):
    return item['nota']
alunos.sort(key=ordena)
alunos_aglomerados =  groupby(alunos, ordena)


for agrutamento, valor_agrupado in alunos_aglomerados:
    valores = list(valor_agrupado)
    print(f'agrupamento: {agrutamento}
    for valor in valores:
        print(f'\t{aluno}')

    quantidade = len(valores)
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
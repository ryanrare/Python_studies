import csv

cadastro = 
with open ('cadastros.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)

    for dado in dados:
        print(dado)

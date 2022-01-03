from zipfile import Zipfile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'CAMINHO/DA/PASTA'

# ESCREVE

with Zipfile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho,arquivo)
        zip.write(caminho_completo, arquivo)

with Zipfile('arquivo.zip', 'r') as zip:
    for arquivo in zip.listanome():
        print(arquivo)

with Zipfile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
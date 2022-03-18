import pywhatkit as kit
from datetime import datetime

# roda esses comandos:
# sudo apt-get install python3-tk python3-dev
# pip3 install pywhatkit

# Se o pywhatkit ainda estiver vermelho no import,
# basta deixar o mouse em cima dele e clicar em instalar, que a ide instala pra vc


# deixe uma guia do navegador aberto que tenha acesso ao seu whatsapp web.
# (não é preciso deixar aberto no wpp, so na guia)

# Aqui tem que colocar o numero que quer ( so o numero sem o 9 )
numero = '86129854'

espacamento = "*" * 10
print(espacamento, "Seja bem vindo a marmitaria", espacamento)

resposta = 'sim'
lista_pratos = list()


def finalizar():
    print(espacamento * 5)
    print("Obrigado por usar o meu programa!")
    print("Adeus")
    exit(0)


while resposta != 'nao':
    print("O que deseja fazer? ")
    print()
    print("1- Cadastrar prato")
    print("2- Ver pratos cadastrados")
    print("3- Apagar algum prato")
    print("4- para enviar a mensagem")

    opcao = int(input("Digite o numero correspondentes a sua opção: "))
    while opcao not in range(1, 6):
        print(espacamento * 5)
        print("Por favor Digite uma das opcoes abaixo : ")
        print("1- Cadastrar prato")
        print("2- Ver pratos cadastrados")
        print("3- Apagar algum prato")
        print("4- para enviar a mensagem")
        print("5 para Sair")
        opcao = int(input("Opção Selecionada : "))

    if opcao == 1:
        qtd_pratos = int(input("Quantos pratos serão cadastrados ? "))
        x = 0
        while x < qtd_pratos:
            prato = str(input(f'Qual o nome do prato {len(lista_pratos) + 1} ? : '))
            lista_pratos.append(prato)
            x += 1
        resposta = str(input("Deseja fazer outra operação? (sim) ou (nao) :"))
        if resposta == 'nao':
            finalizar()

    elif opcao == 2 and len(lista_pratos) > 0:
        for indice, prato in enumerate(lista_pratos):
            print(f'Prato {indice + 1} : {prato}')
        resposta = str(input("Deseja fazer outra operação? (sim) ou (nao) :"))
        if resposta == 'nao':
            finalizar()

    elif opcao == 3:
        for indice, prato in enumerate(lista_pratos):
            print(f'Prato {indice + 1} : {prato}')
        apagar_prato = (int(input("Qual prato deseja apagar ? ")) - 1)

        del lista_pratos[apagar_prato]
        print("Registro apagado com sucesso.")
        resposta = str(input("Deseja fazer outra operação? (sim) ou (nao) :"))
        if resposta == 'nao':
            finalizar()

    elif opcao == 4:
        horas = int(datetime.now().strftime("%H"))
        minutos = int(datetime.now().strftime("%M")) + 1
        kit.sendwhatmsg(f"+55319{numero}",
                        f"Os pratos cadastrados hoje foram: {lista_pratos}", horas, minutos)

        resposta = str(input("Deseja fazer outra operação? (sim) ou (nao) :"))
        if resposta == 'nao':
            finalizar()


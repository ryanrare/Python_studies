print()
print('texto explicativo')

perguntas = {'pergunta 1' : {'pergunta' : 'quanto é 2x2?', 'respostas' : {'a' : '3',
                                                                         'b' : '4',
                                                                         'c' : '32'},
                                                                         'resposta_correta' : 'b'},
             'pergunta 2' : {'pergunta' : 'quanto é 3+4?', 'respostas' : {'a' : '7',
                                                                         'b' : '3',
                                                                         'c' : '2'},
                                                                        'resposta_correta' : 'a'},}
print()
respostas_certas = 0
for pergunta, dadospergunta in perguntas.items():
    print(f'{pergunta}: {dadospergunta["pergunta"]}')

    print('respostas;')
    for resposta, dadosresposta in dadospergunta['respostas'].items():
        print(f'{resposta}: {dadosresposta}')

    respostaDoUsario = input('digite a resposta: ')

    if respostaDoUsario == dadospergunta['resposta_correta']:
        print('acertou!!! top de mais')
        print()
    else: print('talvez na proxima amigo...')
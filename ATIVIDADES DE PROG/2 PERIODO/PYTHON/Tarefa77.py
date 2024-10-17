#Exercício  Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ['TRABALHO', 'FACULDADE', 'AMIGOS', 'JOGOS', 'AMOR', 'NAMORO', 'FALTA', 'SONO', 'DORMIR', 'ACADEMIA', 'REPETIR']
for c in range (0,11):
    print('Para a palavra {} possui as vogais: '.format(palavras[c]), end='')
    if 'A' in palavras[c]:
        print('a', end=' ')
    if 'E' in palavras[c]:
        print('e', end=' ')
    if 'I' in palavras[c]:
        print('i', end=' ')
    if 'O' in palavras[c]:
        print('o', end=' ')
    if 'U' in palavras[c]:
        print('u', end=' ')
    print(end='\n')

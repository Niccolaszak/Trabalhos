#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra','Papel', 'Tessoura')
computador = randint(0,2)
print('Suas opções: ')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESSOURA')
jogador = int(input('Qual sua jogada: '))
print('=='*5)
print('O Computador jogou: {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador-1]))
print('=='*5)
if computador == 0:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    elif jogador == 3:
        print('COMPUTADOR GANHOU')
elif computador == 1:
    if jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR GANHOU')
elif computador == 2:
    if jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    elif jogador == 3:
        print('EMPATE')

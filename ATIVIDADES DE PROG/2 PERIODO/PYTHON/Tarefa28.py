#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
num = randint(1, 5)
num2 = int(input('Adivinhe o numero:'))
if num2 == num:
    print('Parabens você acertou')
else:
    print('Você errou o numero era {}'.format(num))
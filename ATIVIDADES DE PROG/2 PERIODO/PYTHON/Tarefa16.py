#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Insira um numero Real qualquer: '))
print('A parte real de {} é {}'.format(num, trunc(num)))
#Tambem funcionando sem modulos
print('A parte real de {} é {}'.format(num, int(num)))
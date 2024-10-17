#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Insira um numero para saber seu fatorial: '))
f = factorial(n)
c = n
while c > 0:
    print('{}'.format(c), end=' x ' if c > 1 else' = ')
    c -= 1
print(f)
print('O Valor de {}! é {}'.format(n, f))

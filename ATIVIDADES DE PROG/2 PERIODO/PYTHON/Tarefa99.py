'''Exercício  Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(a, b):
    if a > b:
        b = a
    return b
b = 0
for i in range (0,5):
    a = int(input('Insira um numero: '))
    b = maior(a, b)
print('O maior numero digitado foi {}'.format(b))
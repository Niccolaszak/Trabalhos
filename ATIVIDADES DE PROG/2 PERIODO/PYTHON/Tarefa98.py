'''Exercício  Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1                           
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada'''
from time import sleep
def contador(i,f,p):
    print('CONTAGEM +10 DO INICIO')
    for c in range (i, i+10, 1):
        print(f'{c} ', end='')
    print()
    print('CONTAGEM -10 DO FIM')
    for c in range (f, f-10, -2):
        print(f'{c} ', end='')
    print()
    print('CONTAGEM PERSONALIZADA')
    for c in range (i, f, p):
        print(f'{c} ', end='')
inicio = int(input("insira um numero para começar a contagem: "))
fim = int(input("insira um numero para terminar a contagem: "))
passo = int(input("Insira de quantos em quantos quer a contagem: "))
contador(inicio,fim,passo)
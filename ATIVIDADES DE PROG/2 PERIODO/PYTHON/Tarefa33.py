#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('insira o terceiro número: '))
maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
if n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1
print('O maior numero é {} e o menor é {}'.format(maior, menor))
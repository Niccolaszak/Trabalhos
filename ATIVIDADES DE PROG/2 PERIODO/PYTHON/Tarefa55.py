#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 9999
for i in range(0,5):
    peso = float(input('Qual o peso da {}° pessoa: '.format(i+1)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {} e o meno {}'.format(maior,menor))
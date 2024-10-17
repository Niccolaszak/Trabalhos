#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for i in range(0, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu: '.format(i)))
    idade = anoatual-ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tivemos {} maiores e {} menores'.format(maior, menor))
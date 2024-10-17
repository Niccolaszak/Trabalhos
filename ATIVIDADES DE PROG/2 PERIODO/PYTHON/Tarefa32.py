#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano deseja analisar:'))
if ano % 4 == 0:
    print('O ano {} é Bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))

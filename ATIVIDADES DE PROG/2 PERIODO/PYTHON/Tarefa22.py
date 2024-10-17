#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome:'))
min = nome.lower()
max = nome.upper()
quant = len(nome)-nome.count(' ')
div = nome.split()
pnome = len(div[0])
print('Tudo min: {}\nTudo max: {}\nQuantidade de letras: {}\nQuantidade no primeiro nome: {}'.format(min, max, quant, pnome))
# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Insira o preço do produto: '))
print('O preco do produto com um desconto de 5% eh R${}'.format(preco-(preco*0.05)))
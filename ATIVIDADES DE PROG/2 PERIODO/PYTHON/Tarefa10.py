#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input('Quanto dinheiro voce quer converter: R$ '))
print('A quantia de R${:.2f} eh equivalente a US${:.2f}'.format(dinheiro, dinheiro/5.43))
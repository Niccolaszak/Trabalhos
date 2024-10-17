#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
#e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
sorteio = (int(randint(1,10)), int(randint(1,10)), int(randint(1,10)), int(randint(1,10)), int(randint(1,10)))
print("os valores sorteados foram: ")
print(sorteio)
print("O maior valor foi: {}".format(max(sorteio)))
print("o menor valor foi: {}".format(min(sorteio)))
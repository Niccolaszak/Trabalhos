#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
c1 = float(input('Digite op valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
hip = hypot(c1, c2)
print('A Hipotenusa é ', hip)
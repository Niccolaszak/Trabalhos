#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo qualquer: '))
print('Considerando {:.2f}\nO seno é {:.2f}\nO cosseno é {:.2f}\nE a tangente é {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
#Lembrar de usar radians quando for graus de geometria
#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura*altura
quantia = area/2
print('A parede {} de largura por {} de altura, tem a area de {} \nLogo sera necessario {}L de tinta.'.format(largura, altura, area, quantia))
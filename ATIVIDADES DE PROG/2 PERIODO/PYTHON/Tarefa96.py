#Exercício  Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    area = l*c
    return area

l = float(input('Insira a largura do terreno: '))
c = float(input('Insira o comprimento do terreno: '))
a = area(l,c)
print(f'A area do terreno é {a}')
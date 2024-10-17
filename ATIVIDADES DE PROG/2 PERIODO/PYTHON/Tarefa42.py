#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
l1 = float(input('Insira o primeiro lado: '))
l2 = float(input('Insira o segundo lado: '))
l3 = float(input('Insira o terceiro lado: '))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
    print('Os segmentos podem formar um triângulo:') 
    if l1 == l2 == l3:
        print('O triangulo é EQUILÀTERO')
    elif l1 == l2 != l3 or l1 != l2 == l3 or l2 != l1 == l3:
        print('O triangulo é ISÓSCELES')
    elif l1 != l2 != l3:
        print('O triangulo é ESCALENO')
else:
    print('Os segmentos não formam um triângulo')
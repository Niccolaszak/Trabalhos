#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Escreva um valor em Metros: '))
print(' O Valor De {:.2f}m \n Eh igual a {:.2f}cm \n E igual a {:.2f}mm'.format(n, n*100, n*1000))
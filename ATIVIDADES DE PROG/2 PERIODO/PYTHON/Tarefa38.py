#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
if n1 > n2:
    print('O primeiro numero é maior')
elif n1 < n2:
    print('O Segundo numero é maior')
elif n1 == n2:
    print('Os Dois numeros são iguais')
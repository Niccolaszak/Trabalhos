#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um numero: '))
a = num-1
s = num+1
print('Analisando o numero {}'.format(num))
print('O antecessor de {} eh {} '.format(num, a))
print('O sucessor de {} eh {} '.format(num, s))
#Fazendo de outra forma para utilizar menos memoria do sistema
print('Analisando o numero {}'.format(num))
print('O antecessor de {} eh {} e o sucessor eh {}'.format(num, (num-1), (num+1)))
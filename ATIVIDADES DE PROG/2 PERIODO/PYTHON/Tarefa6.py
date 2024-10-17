#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero: '))
print('Usando o numero {} \n O dobro eh {} \n O triplo eh {} \n A raiz quadrada eh {:.3f}'.format(n, n*2, n*3, n**(1/2)))
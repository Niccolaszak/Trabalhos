#Exercício  Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n = 0
tot = 0
c = 0
while n!=999:
    n=int(input('Digite um numero(999-para sair ): '))
    tot += n
    c += 1
print('Você digitou o numero de saida')
print('Você digitou {} numeros e a soma total deles foi {}'.format(c,tot-999))
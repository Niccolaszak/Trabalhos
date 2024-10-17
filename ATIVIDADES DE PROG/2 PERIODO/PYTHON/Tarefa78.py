#Exercício  Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
#mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valor = []
maior = 0
menor = 0
for c in range (0, 5):
    valor.append(int(input('Insira o {} numero: '.format(c))))
    if c == 0:
        maior = menor = valor[c]
    elif valor[c] > maior:
        maior = valor[c]
    elif valor[c] < menor:
        menor = valor[c]
print('Você digitou os valores {}'.format(valor))
print('O maior valor é {}, nas posições: '.format(maior))
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}, ', end='') 
print()
print('O menor valor é {}, nas posições: '.format(menor))
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}, ', end='')
print() 

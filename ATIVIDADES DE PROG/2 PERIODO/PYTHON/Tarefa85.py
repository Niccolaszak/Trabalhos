#Exercício  Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
junto = [[], []]
for i in range (0,7):
    n = int(input(f'Insira o {i+1}° numero: '))
    if n%2 == 0:
        junto[0].append(n)
    else:
        junto[1].append(n)
junto[0].sort()
junto[1].sort()
print(f'Os numeros digitados separados entre pares e impares são: ')
print(f'PARES: {junto[0]}')
print(f'IMPARES: {junto[1]}')
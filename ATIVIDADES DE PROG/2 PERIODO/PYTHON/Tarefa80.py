#Exercício  Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
#Aula Anterior
lista = []
for c in range (0,5):
    n = int(input(f'Insira o {c+1}° numero: '))
    lista.append(n)
print(f'Os valores digitados foram {lista}')
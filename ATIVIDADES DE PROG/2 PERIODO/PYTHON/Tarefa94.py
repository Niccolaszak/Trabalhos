#Exercício  Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre: 
#A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
lista = list()
mulheres = list()
acima = list()

while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Insira o Nome: '))
    pessoa['Sexo'] = str(input('Insira o Sexo(F/M): '))
    pessoa['Idade'] = int(input('Insira a idade: '))
    lista.append(pessoa)
    esc = str(input('Deseja inserir outra pessoa(S/N): '))
    if esc in 'Nn':
        break

totid = 0
for c in range(len(lista)):
    totid += lista[c]['Idade']
medid = totid / len(lista)

for i in range(len(lista)):
    if lista[i]['Sexo'] in 'Ff':
        mulheres.append(lista[i])

for l in range(len(lista)):
    if lista[l]['Idade'] > medid:
        acima.append(lista[l])

print('--' * 20)
print(f'Foram cadastradas {len(lista)} pessoas no total')
print(f'A média das idades é {medid:.2f}')
print('A listagem das mulheres ficou: ')
print(mulheres)
print('E estas são as pessoas mais velhas que a média: ')
print(acima)
print('--' * 20)

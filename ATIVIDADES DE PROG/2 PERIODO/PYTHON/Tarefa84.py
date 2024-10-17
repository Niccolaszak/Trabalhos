'''Exercício  Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
dados = []
reg = []
mai = men = 0
while True:
    dados.append(str(input('Insira o nome de uma pessoa: ')))
    dados.append(float(input('Insira o peso desta pessoa: ')))
    if len(reg) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]
    reg.append(dados[:])
    dados.clear()
    esc = str(input('Deseja inserir outra pessoa(S/N): '))
    if esc in "nN":
        break
print('Você registrou {} pessoas.'.format(len(reg)))
print(f'O maior peso foi {mai} e o menor foi {men}')
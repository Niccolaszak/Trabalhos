#Exercício  Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep
id = list()
while True:
    jogador = dict()
    golpartidas = list()
    jogador['Nome'] = str(input('Insira o nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    total = 0
    for c in range(0,jogador['Partidas']):
        golpartidas.append(int(input(f'Quantos gols na {c+1}° partida: ')))
        total+=golpartidas[c]
    jogador['Gols por partida'] = golpartidas
    jogador['Total de gols'] = total
    jogador['Media de gols'] = total/jogador['Partidas']
    id.append(jogador)
    esc = str(input('Deseja inserir outro Jogador?(S/N): '))
    if esc in 'Nn':
        break

print('+=+'*10)
for i in range (0,len(id)):
    print(f'{id[i]['Nome']} {id[i]['Gols por partida']} {id[i]['Total de gols']} {id[i]['Partidas']} {id[i]['Media de gols']:.2f}')
print('+=+'*10)
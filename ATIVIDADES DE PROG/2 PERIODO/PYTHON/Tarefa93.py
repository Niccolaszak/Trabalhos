jogador = dict()
jogador['Nome'] = str(input('Insira o nome do jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
partidas = list()
total = 0
for c in range(0,jogador['Partidas']):
    partidas.append(int(input(f'Quantos gols na {c+1}° partida: ')))
    total+=partidas[c]
jogador['Total de gols'] = total
print('+=+'*10)
for k,v in jogador.items():
    print(f"{k} é {v}")
print('Sendo eles respectivamente:')
print(partidas)
print('+=+'*10)

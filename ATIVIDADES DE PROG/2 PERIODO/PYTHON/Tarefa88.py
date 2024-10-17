#Exercício  Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
q = int(input('Insira quantos jogos quer gerar: '))
jogos = list()
while len(jogos) < q:
    aposta = list()
    while len(aposta) < 6:
        num = random.randint(1, 60)
        if num not in aposta:
            aposta.append(num)
    aposta.sort()
    if aposta not in jogos:
        jogos.append(aposta)
print('Os jogos gerados foram:')
for b in range (q):
    print(f'{b+1}° = {jogos[b]}')
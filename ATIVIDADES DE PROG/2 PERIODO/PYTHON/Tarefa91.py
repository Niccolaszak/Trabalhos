#Exercício  Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(1,20),
        'jogador2' : randint(1,20),
        'jogador3' : randint(1,20),
        'jogador4' : randint(1,20)}
rank = dict()
for k,v in jogo.items():
    print(f'{k} tirou {v} no D20')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse = True)
i = 1
print('-'*25)
for k,v in rank:
    print(f'{i}° - {k} com {v}')
    sleep(1)
    i+=1
print('-'*25)

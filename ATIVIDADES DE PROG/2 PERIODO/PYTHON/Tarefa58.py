#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador
#vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites
#foram necessários para vencer.
from random import randint
num = randint(1, 10)
acerto = 0
tenta = 0
while acerto == 0:
    num2 = int(input('Adivinhe o numero:'))
    if num2 == num:
        print('Parabens você acertou o numero era {}, Levou {} tentativas'.format(num, tenta))
        acerto = 1
    else:
        print('Você errou tente novamente')
        acerto = 0
        tenta += 1
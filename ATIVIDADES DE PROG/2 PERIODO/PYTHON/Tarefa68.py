#Exercício  Python 68: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
#consecutivas que ele conquistou no final do jogo.
from random import randint
nc = 0
nj = 0
esc = ''
vit = 0
while True:
    nc = randint(0,10)
    esc = str(input('Quer jogar como par ou impar?')).upper()
    if esc == 'IMPAR':
        nj = int(input('Escolha qual numero jogar de 0 a 10:'))
        if (nc+nj)%2 == 0:
            print('Você jogou {} eu joguei {} deu {} que é par então você perdeu'.format(nj,nc,nc+nj))
            break
        else:
            print('Você jogou {} eu joguei {} deu {} que é impar então você Ganhou'.format(nj,nc,nc+nj))
            vit += 1
            print('VAMOS DENOVO')
    if esc == 'PAR':
        nj = int(input('Escolha qual numero jogar de 0 a 10:'))
        if (nc+nj)%2 == 0:
            print('Você jogou {} eu joguei {} deu {} que é par então você Ganhou'.format(nj,nc,nc+nj))
            vit += 1
            print('VAMOS DENOVO')
        else:
            print('Você jogou {} eu joguei {} deu {} que é impar então você perdeu'.format(nj,nc,nc+nj))
            break
print('Infelizmente você perdeu, mas ganhou {} rodadas'.format(vit))
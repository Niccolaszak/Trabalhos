#Exercício  Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
n = 0
while n >= 0:
    n = float(input('Insira um numero(Insira uma valor negativo para sair): '))
    for c in range(1,11):
        print('{} X {} = {}'.format(n,c,n*c))
print('Programa finalizado')
    
#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
sair = False
novos = False
while not sair:
    n1 = float(input('Insira o primeiro numero: '))
    n2 = float(input('Insira o segundo numero: '))
    novos = False
    while not novos:
        print('Escolha uma das opções: ')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair do programa')
        esc = int(input('Sua escolha: '))
        if esc == 1:
            print('A soma de {} + {} é {}\n'.format(n1, n2, n1+n2))
        elif esc == 2:
            print('A multiplicação de {} * {} é {}\n'.format(n1, n2, n1*n2))
        elif esc == 3:
            if n1 > n2:
                print('O numero {} é maior que {}'.format(n1, n2))
            else:
                print('O numero {} é maior que {}'.format(n2, n1))
        elif esc == 4:
            novos = True
        elif esc == 5:
            novos = True
            sair = True
print('Programa finalizado')
#Exercício  Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
n50 = 0
n20 = 0
n10 = 0
n1 = 0
valor = int(input('Insira um valor inteiro para o saque: R$'))
n50 = valor//50
if valor % 50 != 0:
    n20 = (valor%50)//20
    if (valor%50) % 20 != 0:
        n10 = ((valor%50)%20)//10
        if ((valor%50)%20)%10 != 0:
            n1 = ((valor%50)%20)%10//1
print('Serão utilizadas:\n{:.0f} de R$50.00\n{:.0f} de R$20.00\n{:.0f} de R$10.00\n{:.0f} de R$1.00'.format(n50,n20,n10,n1))

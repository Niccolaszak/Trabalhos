#Exercício  Python 72: Crie um programa que 
#tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove","Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis","Dezessete", "Dezoito", "Dezenove", "Vinte")
loop = True
while loop == True:
    n  = int(input('Insira um numero de 0 a 20: '))
    if n > 20 or n < 0:
        print('Valor invalido tente novamente')
    else:
        for c in range(0,20):
            if n-1 == c:
                print('{} por extenso é {}'.format(n,contagem[c]))
                loop=False
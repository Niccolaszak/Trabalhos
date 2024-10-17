#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
#se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoatual = date.today().year
ano = int(input('Informe o ano do seu nascimento: '))
idade = anoatual-ano
if idade > 18:
    print('Você já deveria estar alistado a {} anos'.format(idade-18))
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
elif idade==18:
    print('Você deve se alistar neste ano')
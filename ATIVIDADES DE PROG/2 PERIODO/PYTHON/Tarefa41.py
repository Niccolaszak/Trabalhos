#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#cima de 25 anos: MASTER
from datetime import date
ano = int(input('Insira seu ano de nascimento: '))
idade = date.today().year-ano
print('A sua categoria considerando sua idade de {} é:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14 and idade > 9:
    print('INFANTIL')
elif idade <= 19 and idade > 14:
    print('JUNIOR')
elif idade <= 25 and idade > 19:
    print('SENIOR')
elif idade > 25:
    print('MASTER')
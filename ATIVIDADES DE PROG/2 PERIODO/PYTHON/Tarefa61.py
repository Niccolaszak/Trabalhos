#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
c = 0
p1 = float(input('Insira o primeiro term da PA: '))
ra = float(input('Insira a Razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
while c < 10:
    print(p1,end=", ")
    p1=p1+ra
    c +=1
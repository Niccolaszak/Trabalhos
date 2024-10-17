#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p1 = float(input('Insira o primeiro term da PA: '))
ra = float(input('Insira a Razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
for c in range (0, 10):
    print(p1,end=", ")
    p1=p1+ra
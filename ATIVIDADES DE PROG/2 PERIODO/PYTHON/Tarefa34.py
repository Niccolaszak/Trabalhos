#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o sálario para o aumento: '))
if sal > 1250:
    print('Seu salario era {:.2f} e agora é {:.2f}'.format(sal, sal+(sal*0.1)))
else:
    print('Seu sálario era {:.2f} e agora é {:.2f}'.format(sal, sal+(sal*0.15)))
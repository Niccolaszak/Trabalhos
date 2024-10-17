# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Insira o salario para efetuar o aumento: '))
print('Seu salario era de R${:.2f} e com o aumento de 15% ficou R${:.2f}'.format(salario, salario+(salario*0.15)))
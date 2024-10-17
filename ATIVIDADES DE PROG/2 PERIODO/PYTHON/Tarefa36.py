#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal 
#não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Insira  valor da casa: '))
salário = float(input('Insira seu salario mensal: '))
anos = float(input('Insira em quantos anos vai pagar: '))
prestmes = valor/(anos*12)
salario30 = salário*0.3
if salario30 == prestmes or salario30 > prestmes:
    print('O Emprestimo foi aprovado')
elif  salario30 < prestmes:
    print('O emprestimo foi recusado')
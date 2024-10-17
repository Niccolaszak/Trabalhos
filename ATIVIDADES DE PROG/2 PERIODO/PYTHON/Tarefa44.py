#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros
valor = float(input('Insira o valor do produto: '))
print('Qual será o metodo de pagamento?')
print('[1] A vista no dinheiro/cheque.')
print('[2] A vista no Cartão.')
print('[3] Em 2x no cartão.')
print('[4] Em 3x ou mais no Cartão.')
esc = float(input('Insira o numero: '))
if esc == 1:
    print('O valor era {:.2f} e pagando a vista no dinheiro/cheque fica {:.2f}'.format(valor, valor-(valor*0.1)))
elif esc == 2:
    print('O Valor era {:.2f} e pagando a visa no cartao fica {:.2f}'.format(valor, valor-(valor*0.05)))
elif esc == 3:
    print('O Valor era {:.2f} pagando em 2x no cartão fica {:.2f}'.format(valor,valor))
elif esc == 4:
    print('o valor era {:.2f} e pagando em 3x ou mais no cartao fica {:.2f}'.format(valor, valor+(valor*0.2)))
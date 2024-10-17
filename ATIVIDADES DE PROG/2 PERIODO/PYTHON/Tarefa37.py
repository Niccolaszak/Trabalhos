#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Insira um numero: '))
print('Escolha uma das bases para conversão:\n')
print('[1] Converter para binário\n')
print('[2] Converter para octal\n')
print('[3] Converter para hexadecial\n')
esc = int(input('Sua escolha: '))
if esc == 1:
    print('O numero {} em binario fica {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('O numero {} em Octal fica {}'.format(num, oct(num)[2:]))
else:
    print('O numero {} em Hexadecimal fica {}'.format(num, hex(num)[2:]))
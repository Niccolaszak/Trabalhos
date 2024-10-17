#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = float(input('Insira um numero: '))
print('A tabuada deste numero é: ')
for c in range (1, 10):
    print('{} X {} = {}'.format(num, c, num*c))
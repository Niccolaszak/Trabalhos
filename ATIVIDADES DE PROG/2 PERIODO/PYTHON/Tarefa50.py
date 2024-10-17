#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
count = 0
for c in range(0, 6):
    num = float(input('Insira o {} numero:'.format(c+1)))
    if num%2 == 0:
        soma = soma + num
        count = count + 1
print('A somatoria dos {} numeros pares é: {}'.format(count, soma))
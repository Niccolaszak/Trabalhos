#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
#ao usuário se ele quer ou não continuar a digitar valores.
n = 0
tot = 0
c = 0
maior = 0
menor = 99999999999999
esc = False
while not esc:
    n = int(input('Digite um valor: '))
    tot += n
    c += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if c %5 == 0:
        vai = str(input('Deseja incluir mais 5 numeros?(S/N)')).lower()
        if vai == 'n':
            esc = True
media = tot/c
print('Loop finalizado')
print('Escreveu {} Valores e a soma total foi {}'.format(c, tot))
print('No qual {} foi o maior e {} foi o menor'.format(maior, menor))
print('A media total foi {}'.format(media))
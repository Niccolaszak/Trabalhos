#Exercício  Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
tot = 0
prot1000 = 0
maisbarato = ''
menor = 9999999999999999
esc = 'S'
while True:
    preço = float(input('Insira o preço do produto: '))
    nome = str(input('Insira o nome do produto: ')).upper()
    tot += preço
    if preço > 1000:
        prot1000 +=1
    if  preço < menor:
        menor = preço
        maisbarato = nome
    esc = str(input('Deseja continuar inserindo produtos(S/N)?')).upper()
    while esc not in('SN'):
        esc = str(input('Escolha invalida tente novamente, Deseja continuar inserindo produtos(S/N)?')).upper()
    if esc == 'N':
        break
print('O total foi R${:.2f} , {} Produtos custam mais de R$1000.00, {} Foi o produto mais barato custando {:.2f}'.format(tot,prot1000,maisbarato,menor))
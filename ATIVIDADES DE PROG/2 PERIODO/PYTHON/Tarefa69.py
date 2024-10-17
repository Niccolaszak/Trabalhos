#Exercício  Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
m18 = 0
hom = 0
mu20 = 0
while True:
    idade = int(input('Insira a idade da pessoa: '))
    sex = str(input('Insira o sexo da pessoa(M/F): ')).upper()
    if idade > 18:
        m18 +=1
    if sex == 'M':
        hom +=1
    if sex == 'F' and idade < 20:
        mu20 +=1
    esc = str(input('Deseja continuar inserindo pessoas(S/N)?')).upper()
    if esc == 'N':
        break
print('Você inseriu {} pessoar maiores de 18 anos, {} Homems, {} mulheres com menos de 20 anos'.format(m18,hom,mu20))
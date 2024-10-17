#Exercício Python 56: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
homemvelho = ''
idadehomemvelho = 0
mediaidade = 0
mulhermenos20 = 0
for i in range (1,5):
    nome = str(input('Insira o nome da {}° pessoa: '.format(i)))
    idade = int(input('Insira a idade da {}° pessoa: '.format(i)))
    sexo = str(input('Insira o sexo da {} pessoa(M/F): '.format(i))).upper()
    mediaidade += idade
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    elif sexo == 'M' and idade > idadehomemvelho:
        homemvelho = nome
print('Neste grupo a media de idade é {} o Homem mais velho se chama {} e há {} mulheres com menos de 20 anos'.format(mediaidade/4, homemvelho, mulhermenos20))
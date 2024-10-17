#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('A media de suas notas é {} então está aprovado'.format(media))
elif media < 7 and media >= 5:
    print('A media das suas notas é {} então está de recuperação'.format(media))
elif media < 5:
    print('A media das suas notas é {} então está reprovado'.format(media))
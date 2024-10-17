#Exercício  Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = list()
while True:
    nome = str(input('Insira o Nome do estudante: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    aluno = list()
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    boletim.append(aluno)
    esc = str(input('Quer inserir mais alunos(S/N)? '))
    if esc in 'nN':
        break
for i in range(len(boletim)):
    print(boletim[i])


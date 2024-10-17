#Exercício  Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
info = dict()
info['nome'] = str(input("Nome: "))
info['media'] = float(input("Media: "))
if info['media'] >= 7:
    info['sit'] = 'Aprovado'
elif info['media'] >= 5 and info['media'] < 7:
    info['sit'] = 'Recuperação'
else:
    info['sit'] = 'Reprovado'
for k,v in info.items():
    print(f'-- {k} é {v}')
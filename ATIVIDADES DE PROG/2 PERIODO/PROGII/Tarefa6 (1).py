#1 - Faça uma função que receba um dicionário e um número N. Apresentar os primeiros N itens e os últimos N itens do dicionário
'''dico = {'numeros':[1,1,2],'tresu': [14,84,52],'tresp': [45,65,12],'nuos':[10,18,42],'tru': [140,844,562],'tesp': [435,615,142]}
def funcao(dic,n):
    a = list(dic.keys())
    b = list(dic.values())
    print(f"OS {n} primeiros valores são: ")
    for i in range(n):
        print(a[i],b[i])
    print(f"OS {n} Ultimos valores são: ")
    for i in range(1,n+1):
        print(a[-i],b[-i])
a = int(input("Insira um numero(de 0 a 5): "))
funcao(dico,a)'''
#2 - Faça uma função que troca as chaves e os valores de lugar (Exemplo "chave" : "Valor" vira -> "Valor" : "chave")
'''dici = {'Um' : 1, 'Dois' : 2, 'Tres' : 3}
def troca(dic):
    return {valor: chave for chave, valor in dic.items()}
inverso = troca(dici)
print(inverso)'''
alunos = dict()
while True:
    nome = str(input('Insira o nome do aluno: '))
    alunos[nome] = []
    for i in range(0,3):
        alunos[nome].append(float(input(f'Insira a {i+1}° nota: ')))
    continua = True
    esc = 'f'
    esc = str(input("deseja inserir outro aluno(N para não)? "))
    if esc == 'N' or esc == 'n':
        break
print("==="*20)
medias = list()
for k,v in alunos.items():
    soma = 0
    for i in range(0,3):
        soma += alunos[k][i]
    med = soma/3
    medias.append(med)
i = 0
for k,v in alunos.items():
    print(f'A media do aluno {k} foi de {medias[i]:.2f}')
    i+=1
print("==="*20)
for k,v in alunos.items():
    sorted(alunos[k])
    print(f'A maior nota do aluno {k} foi {alunos[k][-1]} e a menor nota foi {alunos[k][0]}')
print("==="*20)
mediasorg = sorted(medias)
maior = mediasorg[-1]
menor = mediasorg[0]
posima = medias.index(maior)
posime = medias.index(menor)
nomes = list(alunos.keys())
print(f"A maior media foi do aluno {nomes[posima]} com {medias[posima]:.2f} de media.")
print(f"A menor media foi do aluno {nomes[posime]} com {medias[posime]:.2f} de media.")
print("==="*20)
print('As Notas e medias de cada uluno ficou:')
j = 0
for k,v in alunos.items():
    print(f"{k}: {v}; Média:{medias[j]:.2f}")
    j+=1
print("==="*20)
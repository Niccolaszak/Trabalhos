def nota(notas):
    maior_nota = 0
    menor_nota = notas[0]
    for i in range (len(notas)):
        if notas[i]>maior_nota:
            maior_nota = notas[i]
        if notas[i]<menor_nota:
            menor_nota = notas[i]
    soma = 0
    for i in range (len(notas)):
        soma+=notas[i]
    media = soma/len(notas)
    situação = ""
    if media >= 70:
        situação = "Turma Aprovada"
    if media < 70 and media >= 40:
        situação = "Precisa de melhora"
    if media < 40:
        situação = "Pqp tudo burro"
    info = {'Maior nota' : maior_nota,
        'Menor nota' : menor_nota,
        'Media da turma' : media,
        'Situação' : situação
    }
    return info
alunos = [20,50,70,80,90,60,70,80,90,50,70,80,80]
print(nota(alunos))

#OU

def aula(n):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if r['Media'] >= 70:
        r['Situação'] = "Aprovada"
    if r['Media'] < 70 and r['Media'] >= 40:
        r['Situação'] = "Melhorem"
    if r['Media'] < 40:
        r['Situação'] = "Tudo burro"
    return r
r = [20,50,70,80,90,60,70,80,90,50,70,80,80]
print(aula(r))
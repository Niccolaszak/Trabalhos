#Exercício  Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente. 
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
c = 1
while True:
    lista.append(int(input(f'Digite o {c}º numero(Digite -1 para parar): ')))
    c+=1
    if -1 in lista:
        lista.pop()
        break
print(f'Os valores digitados foram {lista}.')
print(f'Foram um total de {len(lista)} valores digitados.')
lista.sort(reverse=True)
print(f'A Lista eordem decrescente: {lista}')
if 5 in lista:
    print(f'O 5 esta na lista na posição {lista.index(5)}')
else:
    print('O 5 não está na lista')
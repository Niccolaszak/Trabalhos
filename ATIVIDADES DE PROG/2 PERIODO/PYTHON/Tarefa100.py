#Exercício  Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
total=0
def sorteia(n):
    while len(n) < 5:
        m = randint(0,10)
        if m not in n:
            n.append(m)
    return n
def somapar(n):
    total=0
    for i in range(0,5):
        if n[i] %2 == 0:
            total+=n[i]
    return total
numeros = list()
sorteia(numeros)
print(numeros)
total = somapar(numeros)
print('A soma dos pares é {}'.format(total))
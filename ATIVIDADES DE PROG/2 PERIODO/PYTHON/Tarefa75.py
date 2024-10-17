#Exercício  Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
lista = (int(input("Digite um numero: ")), int(input("Digite outro numero: ")), int(input("Insira outro: ")), int(input("Insira o ultimo: ")))
noves = 0
print("O valor 9 apareceu {} vezes".format(lista.count(9)))
if 3 in lista:
    print("Ovalor 3 apareceu primeiro na posição: {}".format(lista.index(3)))
else:
    print("O 3 não esta na lista")
print("Os numeros pares digitados são:")
for c in range(0,len(lista)):
    if lista[c]%2 == 0:
        print(lista[c], end=' ')

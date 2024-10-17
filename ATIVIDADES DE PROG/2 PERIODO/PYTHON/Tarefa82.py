#Exercício  Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares = []
impar = []
c=1
while True:
    valores.append(int(input(f'Digite o {c}º numero(Digite -1 para parar): ')))
    c+=1
    if -1 in valores:
        valores.pop()
        break
a = 0
for i in range (0, len(valores)):
    if valores[a]%2==0:
        pares.append(valores[a])
        a+=1
    else:
        impar.append(valores[a])
        a+=1
print(f'Os valores digitatos na primeira lista foram {valores}')
print(f'A lista de valores pares é: {pares}')
print(f'A lista de valores impares é: {impar}')
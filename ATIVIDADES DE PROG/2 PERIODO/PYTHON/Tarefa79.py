#Exercício  Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
#e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, 
#serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
c = 1
esc = 'F'
print('insira valores, digite -1 para parar')
while True:
    n = int(input(f'Insira o {c}° Valor: '))
    if n not in valores:
        valores.append(n)
    if valores[len(valores)-1] == -1:
        break
    c += 1
valores.pop()
valores.sort()
print(f'os valores digitados foram: {valores}')

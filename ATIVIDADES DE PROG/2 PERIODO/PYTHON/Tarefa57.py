#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = ''
while sex != 'F' and sex != 'M':
    sex = str(input('Insira seu sexo(F/M): ')).upper()
    if sex != 'F' and sex != 'M':
        print('Informação invalida tente novamente')
print(sex)

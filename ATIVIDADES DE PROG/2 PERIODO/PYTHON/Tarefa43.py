#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
h = float(input('Insira a sua altura em Metros: '))
p = float(input('Insira o seu peso em Kg: '))
IMC = p/h**2
print("Seu IMC é {:.2f} Logo você está: ".format(IMC))
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC >= 18.5 and IMC < 25:
    print('PESO IDEAL')
elif IMC >= 25 and IMC < 30:
    print('SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print('OBESO')
elif IMC >= 40:
    print('OBESIDADE MÓRBIDA')
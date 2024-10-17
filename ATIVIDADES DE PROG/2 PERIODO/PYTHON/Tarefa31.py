#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dis = float(input('Digite a distancia da viagem em KM: '))
if dis <= 200:
    print('A viagem custará R${:.2f}'.format(dis*0.5))
else:
    print('A viagem custará R${:.2f}'.format(dis*0.45))
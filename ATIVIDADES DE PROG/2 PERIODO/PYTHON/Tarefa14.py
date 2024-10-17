# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura para conversão: '))
print('A temperatura de {:.2f}°C é igual a {:.2f}°F'.format(celsius, (celsius*9/5)+32))
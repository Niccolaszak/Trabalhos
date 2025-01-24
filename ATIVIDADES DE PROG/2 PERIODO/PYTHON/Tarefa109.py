from utilidadesCeV import moeda
a = int(input("digite um numero: "))
b = str(input("deseja ver os numeros foramtados? (1) - Sim (0) - Não "))
print(f"O proximo numero é: {moeda.aumentar(a,b)}")
print(f"e o numero anterior é: {moeda.diminuir(a,b)}")
print(f"o dobro é: {moeda.dobro(a,b)}")
print(f"e a metade é: {moeda.metade(a,b)}")
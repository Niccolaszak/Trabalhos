from utilidadesCeV import moeda
a = int(input("digite um numero: "))
print(f"O numero -10% é {moeda.aumentar(a,1)}, e o numero -10% é {moeda.diminuir(a,1)}, o dobro é {moeda.dobro(a,1)} e a metade é {moeda.metade(a,1)}")
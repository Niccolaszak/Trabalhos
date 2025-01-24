from utilidadesCeV import moeda
a = float(input("Insira um numero para a formatação monetaria: "))
print(f"O numero em dinheiro é: {moeda.moeda(a)}")
print(f"A metade dessa quantia é: {moeda.metade(a,1)}")
print(f"O Dobro dessa quantia é: {moeda.dobro(a,1)}")
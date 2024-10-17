import Tarefa107_moeda
a = float(input("Insira um numero para a formatação monetaria: "))
print(f"O numero em dinheiro é: {Tarefa107_moeda.moeda(a)}")
print(f"A metade dessa quantia é: {Tarefa107_moeda.moeda(Tarefa107_moeda.metade(a))}")
print(f"O Dobro dessa quantia é: {Tarefa107_moeda.moeda(Tarefa107_moeda.dobro(a))}")
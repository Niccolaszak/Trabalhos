import Tarefa107_moeda
a = int(input("digite um numero: "))
b = str(input("deseja ver os numeros foramtados? (1) - Sim (0) - Não "))
print(f"O proximo numero é: {Tarefa107_moeda.aumentar(a,b)}")
print(f"e o numero anterior é: {Tarefa107_moeda.diminuir(a,b)}")
print(f"o dobro é: {Tarefa107_moeda.dobro(a,b)}")
print(f"e a metade é: {Tarefa107_moeda.metade(a,b)}")
import csv

def fib(n):
    resultados = [1,1]
    for i in range(2,n):
            resultado = resultados[-1] + resultados[-2] 
            resultados.append(resultado)
    return resultados

num = int(input("Insira até onde quer ver a sequencia de fibonacci: "))
resultado_fib = fib(num)


arquivo_fat = "fib.csv"


with open(arquivo_fat, mode="w", newline="") as arquivo: 
    escrever_csv = csv.writer(arquivo)
    print(escrever_csv)
    escrever_csv.writerow(["P", "N"])


    for i, numero in enumerate(resultado_fib):
        escrever_csv.writerow([ i+1, numero])
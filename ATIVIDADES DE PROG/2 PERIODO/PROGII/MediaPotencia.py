import pandas as pd

a = pd.read_csv("carros.csv")
print(a)


soma_potencia = a["potencia"].sum()
quantidade = len(a["potencia"])
print(f"A soma de todas as potencias é: {soma_potencia}")
print(f"A quantidade total de potencias somadas é: {quantidade}")
media_potencia = soma_potencia/len(a["potencia"])
print(f"A media das potencias sao: {media_potencia:.2f}")
contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove","Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis","Dezessete", "Dezoito", "Dezenove", "Vinte")
for pos in range (0,20):
    if pos %2 == 0:
        print(contagem[pos], end=' - ')
    else:
        print(contagem[pos])
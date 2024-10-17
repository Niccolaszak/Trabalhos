#Exercício  Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove","Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis","Dezessete", "Dezoito", "Dezenove", "Vinte")
print("os cinco primeiros times sâo {}".format(contagem[0:5]))
print("os quatro ultimos times são {}".format(contagem[17:]))
print("em ordem alfabetica: {}".format(sorted(contagem)))
print("ta na posição {}".format(contagem[16]))
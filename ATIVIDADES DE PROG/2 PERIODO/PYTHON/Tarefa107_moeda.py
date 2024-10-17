def aumentar(n, e):
    b = n+100
    if e == "0":
        return b
    else:
        return moeda(b)
def diminuir(n, e):
    b = n-100
    if e == "0":
        return b
    else:
        return moeda(b)

def dobro(n, e):
    b = n*2
    if e == "0":
        return b
    else:
        return moeda(b)

def metade(n, e):
    b = n/2
    if e == "0":
        return b
    else:
        return moeda(b)

def moeda(n):
    return f"R${n:.2f}"
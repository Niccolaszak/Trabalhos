def aumentar(n, e):
    b = n+n*0.1
    if e == "0":
        z = b
        return z
    else:
        z = moeda(b)
        return z
    
def diminuir(n, e):
    b = n-n*0.1
    if e == "0":
        z = b
        return z
    else:
        z = moeda(b)
        return z

def dobro(n, e):
    b = n*2
    if e == "0":
        z = b
        return z
    else:
        z = moeda(b)
        return z

def metade(n, e):
    b = n/2
    if e == "0":
        z = b
        return z
    else:
        z = moeda(b)
        return z
    
def moeda(n):
    a = f"R${n:.2f}"
    return a

def resumo(n):
    print("Resumo do valor")
    print("-"*30)
    print(f"Preço analisado: {moeda(n)}")
    print(f"Preço pela metade: {metade(n,1)}")
    print(f"Preço pela dobro: {dobro(n,1)}")
    print(f"Preço diminuido em 10%: {diminuir(n,1)}")
    print(f"Preço aumentado em 10%: {aumentar(n,1)}")
    print("-"*30)
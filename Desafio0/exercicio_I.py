

def numero():
    n = int(input("Digite o numero n: "))
    lista = []
    for i in range(1,n+1):
        valor = "*"*i
        lista.append(valor)

    return print(lista)  

numero()

## Resolução do exercício I
def numero():
    n = int(input("Digite o numero n: "))
    lista = ["*"* i for i in range(1, n+1)]
    print(lista)  

    return lista

numero()

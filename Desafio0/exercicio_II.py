
def dif_absoluta(vetor_atual):
    vetor_dif = []
    vetor_ordenado = sorted(vetor_atual)
    print(vetor_ordenado)
    menor_dif = float('inf')

    for a in range(len(vetor_ordenado) - 1):
        diferenca = abs(vetor_ordenado[a] - vetor_ordenado[a+1])

        if diferenca < menor_dif:
            menor_dif = diferenca
            vetor_dif = [(vetor_ordenado[a], vetor_ordenado[a+1])]
            
        elif diferenca == menor_dif:
            vetor_dif.append((vetor_ordenado[a], vetor_ordenado[a+1]))

    return vetor_dif

vetor = [1,3,10, 5]
menor = dif_absoluta(vetor) 
print(menor)


def dif_absoluta(vetor_atual, allow_duplicates=True, sorted_pairs=True, unique_pairs=True):
    if not allow_duplicates:

        if len(set(vetor_atual)) != len(vetor_atual):
            raise Exception('Os pares de número não podem ter valores duplicados')
    
    if sorted_pairs:
        vetor_ordenado = sorted(vetor_atual)
    else:
        vetor_ordenado = vetor_atual[:]

    vetor_dif = []
    
    print(vetor_ordenado)
    menor_dif = float('inf')

    for a in range(len(vetor_ordenado) - 1):
        diferenca = abs(vetor_ordenado[a] - vetor_ordenado[a+1])

        if diferenca < menor_dif:
            menor_dif = diferenca
            vetor_dif = [(vetor_ordenado[a], vetor_ordenado[a+1])]
            
        elif diferenca == menor_dif:
            vetor_dif.append((vetor_ordenado[a], vetor_ordenado[a+1]))

    
    if unique_pairs:
        vetor_dif_unicos = set()
        for (a,b ) in vetor_dif:
            if (a,b) not in vetor_dif_unicos:
                vetor_dif_unicos.add((a,b))
        vetor_dif = list(vetor_dif_unicos)


    return vetor_dif


    

vetor = [1,6, 3,10]
menor = dif_absoluta(vetor) 
print(menor)

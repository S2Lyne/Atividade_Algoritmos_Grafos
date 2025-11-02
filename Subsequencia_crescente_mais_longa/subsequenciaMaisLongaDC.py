import time

cont_dc = 0  # contador global

def Cresc_long(X, a, b):
    
    """
    Entry point DC que faz prints de trace e usa uma função recursiva Ti
    que calcula (comprimento, subsequência) para cada índice.
    Não usa memoização (recalcula subproblemas) — fiel ao enunciado.
    """
    
    if a == b: 
        return [X[a]]

    
    global cont_dc
    cont_dc += 1

    maxt = 0
    maxi = -1
    i = b  
    j = a

    while j < i:
        
        S_j = Cresc_long(X, a, j)
        
        if X[j] < X[i] and len(S_j) > maxt:
            maxt = len(S_j)
            maxi = j
        j += 1
        
    if maxi == -1:
        resultado = [X[i]]
    else:
        resultado = Cresc_long(X, a, maxi) + [X[i]]

    #print(f"Resultado parcial para i={i}: {resultado}")
    return resultado


if __name__ == "__main__":
    
    X = [1,3,2,7,10,14,8,31]
    

    print(X)

    start_time = time.time()
    kl = Cresc_long(X, 0, len(X)-1)
    end_time = time.time()
    print("\nResultado final:", kl)
    print("O comprimento da maior subsequência crescente é:", len(kl))
    print("Chamadas DC:", cont_dc)
    print("Tempo de execução:", end_time - start_time)
# distancia_edicao_PD.py
import time
import numpy as np # Usaremos numpy para facilitar a criação da matriz

cont_pd = 0 # Contador global de operações

def diff(X, i, Y, j):
    """
    Função diff(i,j) dos slides.
    """
    if X[i-1] == Y[j-1]:
        return 0
    else:
        return 1

def C_ij_PD(X, Y):
    """
    Implementação com Programação Dinâmica (bottom-up)
    Baseado no algoritmo da Página 29
    """
    global cont_pd
    n = len(X)
    m = len(Y)

    # Cria a matriz C de (n+1) x (m+1)
    C = np.zeros((n + 1, m + 1), dtype=int)

    # --- Casos Base (i=0 ou j=0) ---
    # 'for i <- 1,2...n do C_i,0 <- i'
    for i in range(n + 1):
        C[i][0] = i
    
    # 'for j <- 1,2...m do C_0,j <- j'
    for j in range(m + 1):
        C[0][j] = j

    # --- Preenche a tabela (Casos i,j > 0) ---
    # 'for i <- 1,2...n do'
    for i in range(1, n + 1):
        # 'for j <- 1,2...m do'
        for j in range(1, m + 1):
            
            cont_pd += 1 # Contando a operação principal (o min)
            
            custo_remocao = C[i-1][j] + 1
            custo_insercao = C[i][j-1] + 1
            custo_subst = C[i-1][j-1] + diff(X, i, Y, j)
            
            # 'C_i,j = min{...}'
            C[i][j] = min(custo_remocao, custo_insercao, custo_subst)

    # O resultado final está no canto inferior direito
    return C[n][m]

# --- Teste (if __name__ == "__main__") ---
if __name__ == "__main__":
    
    # Exemplo dos slides
    X_str = "ABBBAAB" 
    Y_str = "BBAABB"
    n = len(X_str)
    m = len(Y_str)

    print(f"Testando PD com X={X_str} (n={n}), Y={Y_str} (m={m})")

    cont_pd = 0
    start_time = time.time()
    distancia = C_ij_PD(X_str, Y_str)
    end_time = time.time()

    # O resultado 3 bate com o exemplo do slide
    print(f"\nResultado PD: {distancia}") 
    print(f"Operações PD: {cont_pd}")
    print(f"Tempo de execução: {end_time - start_time:.4f}s")
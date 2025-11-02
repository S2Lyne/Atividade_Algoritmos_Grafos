# distancia_edicao_DC.py
import time

cont_dc = 0 # Contador global de chamadas

def diff(X, i, Y, j):
    """
    Função diff(i,j) dos slides.
    Nota: Python usa índice 0, então X[i] dos slides é X[i-1] no código.
    """
    if X[i-1] == Y[j-1]:
        return 0 # 'caso contrário'
    else:
        return 1 # 'se x_i != y_j' (corrigido do slide)

def C_ij_DC(X, i, Y, j):
    """
    Implementação recursiva (DC) da formulação C_ij.
    i = tamanho do prefixo de X
    j = tamanho do prefixo de Y
    """
    global cont_dc
    cont_dc += 1 # Conta a chamada recursiva

    # --- Caso Base (se i=0 ou j=0) ---
    if i == 0:
        return j # 
    if j == 0:
        return i # 

    # --- Caso Recursivo (se i,j > 0) ---
    
    # Custo de Remoção: C_i-1,j + 1
    custo_remocao = C_ij_DC(X, i - 1, Y, j) + 1
    
    # Custo de Inserção: C_i,j-1 + 1
    custo_insercao = C_ij_DC(X, i, Y, j - 1) + 1
    
    # Custo de Substituição/Match: C_i-1,j-1 + diff(i,j)
    custo_subst = C_ij_DC(X, i - 1, Y, j - 1) + diff(X, i, Y, j)

    # min{...} 
    return min(custo_remocao, custo_insercao, custo_subst)


# --- Teste (if __name__ == "__main__") ---
if __name__ == "__main__":
    
    # Exemplo dos slides
    X_str = "ABBBAAB" 
    Y_str = "BBAABB"
    n = len(X_str)
    m = len(Y_str)

    print(f"Testando DC com X={X_str} (n={n}), Y={Y_str} (m={m})")

    cont_dc = 0
    start_time = time.time()
    distancia = C_ij_DC(X_str, n, Y_str, m)
    end_time = time.time()

    print(f"\nResultado DC: {distancia}")
    print(f"Chamadas DC: {cont_dc}")
    print(f"Tempo de execução: {end_time - start_time:.4f}s")
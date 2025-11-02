# subconjunto_soma_PD.py
import time
import numpy as np

cont_pd = 0 # Contador global

def F_PD(A, k):
    """
    Implementação com Programação Dinâmica (bottom-up)
    A = lista de números (o conjunto A)
    k = soma alvo 'k'
    """
    global cont_pd
    cont_pd = 0
    n = len(A)

    # Cria a tabela F[n+1][k+1] (como no slide da Mochila)
    # F[i][j] = True se a soma 'j' é possível com os primeiros 'i' itens
    F = np.full((n + 1, k + 1), False)

    # --- Casos Base ---
    # Soma 0 (j=0) é sempre possível com 0 itens
    for i in range(n + 1):
        F[i][0] = True
        
    # (Soma j > 0 com i=0 já é False por padrão)

    # --- Preenche a tabela (Casos i,j > 0) ---
    for i in range(1, n + 1):
        a_i = A[i-1] # Item i (0-indexado)
        
        for j in range(1, k + 1):
            cont_pd += 1 # Conta a operação principal
            
            # 1. Se o item for maior que a soma, eu sou OBRIGADO a pular
            if a_i > j:
                F[i][j] = F[i-1][j]
            # 2. Senão, eu verifico as duas escolhas
            else:
                F[i][j] = F[i-1][j] or F[i-1][j - a_i]

    # O resultado final está no canto inferior direito
    return F[n][k]

# --- Teste (if __name__ == "__main__") ---
if __name__ == "__main__":
    
    A_teste = [3, 34, 4, 12, 5, 2]
    k_teste = 9
    n = len(A_teste)
    
    print(f"Testando PD com A={A_teste} (n={n}), k={k_teste}")

    cont_pd = 0
    start_time = time.time()
    resultado = F_PD(A_teste, k_teste) # (4+5=9 -> True)
    end_time = time.time()

    print(f"\nResultado PD: {resultado}")
    print(f"Operações PD: {cont_pd}")
    print(f"Tempo de execução: {end_time - start_time:.4f}s")
    
    # Teste 2 (impossível)
    k_teste = 30
    cont_pd = 0
    start_time = time.time()
    resultado = F_PD(A_teste, k_teste)
    end_time = time.time()
    print(f"\nTestando PD com k={k_teste}")
    print(f"Resultado PD: {resultado}")
    print(f"Operações PD: {cont_pd}")
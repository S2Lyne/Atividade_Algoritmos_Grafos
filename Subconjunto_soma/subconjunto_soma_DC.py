# subconjunto_soma_DC.py
import time

cont_dc = 0 # Contador global

def F_DC(A, i, j):
    """
    Implementação recursiva (DC) de Subconjunto Soma.
    A = lista de números (o conjunto A)
    i = "considerar os primeiros 'i' itens de A" (A[0...i-1])
    j = "soma alvo 'j' (o 'k' do problema)"
    """
    global cont_dc
    cont_dc += 1

    # --- Casos Base ---
    # 1. Soma 'j' é 0? SUCESSO (conjunto vazio soma 0)
    if j == 0:
        return True
    
    # 2. Itens 'i' acabaram E soma 'j' > 0? FALHA
    if i == 0 and j > 0:
        return False
        
    # Pega o i-ésimo item (A[i-1] pois A é 0-indexado)
    a_i = A[i-1]

    # --- Casos Recursivos ---
    
    # 3. Se o item atual (a_i) for MAIOR que a soma 'j' que eu quero,
    #    eu SOU OBRIGADO a pular ele.
    if a_i > j:
        return F_DC(A, i - 1, j)
    
    # 4. Se o item for menor ou igual, eu tenho duas escolhas:
    #    OU eu pulo ele (F_DC(A, i-1, j))
    #    OU eu uso ele (F_DC(A, i-1, j - a_i))
    #    Se qualquer um dos caminhos der True, o resultado é True.
    else:
        return F_DC(A, i - 1, j) or F_DC(A, i - 1, j - a_i)


# --- Teste (if __name__ == "__main__") ---
if __name__ == "__main__":
    
    A_teste = [3, 34, 4, 12, 5, 2]
    k_teste = 9
    n = len(A_teste)
    
    print(f"Testando DC com A={A_teste} (n={n}), k={k_teste}")

    cont_dc = 0
    start_time = time.time()
    resultado = F_DC(A_teste, n, k_teste) # (4+5=9 -> True)
    end_time = time.time()

    print(f"\nResultado DC: {resultado}")
    print(f"Chamadas DC: {cont_dc}")
    print(f"Tempo de execução: {end_time - start_time:.4f}s")

    # Teste 2 (impossível)
    k_teste = 30
    cont_dc = 0
    start_time = time.time()
    resultado = F_DC(A_teste, n, k_teste)
    end_time = time.time()
    print(f"\nTestando DC com k={k_teste}")
    print(f"Resultado DC: {resultado}")
    print(f"Chamadas DC: {cont_dc}")
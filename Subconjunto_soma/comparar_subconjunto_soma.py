# comparar_subconjunto_soma.py
import time
import matplotlib.pyplot as plt
import os
import subconjunto_soma_PD as pd_mod
import subconjunto_soma_DC as dc_mod

# --- 1. DEFINA AQUI OS PARES PARA OS EXPERIMENTOS ---
# O alvo 'k' é fixo para cada run, o 'n' (tamanho da lista) varia.
PARES_DE_TESTE = {
    # Run 1: Um caso simples
    "run_1_simples": ([3, 34, 4, 12, 5, 2, 8, 10, 1, 7, 15, 20, 6], 100),
    # Run 2: Um alvo 'k' maior
    "run_2_alvo_alto": ([1, 5, 2, 9, 10, 11, 8, 3, 4, 7, 6, 12, 14], 150),
    # Run 3: Um caso com números maiores
    "run_3_nums_altos": ([20, 31, 12, 5, 42, 50, 10, 3, 22, 19, 33, 25, 17], 200)
}

# Limite de sanidade (DC explode em n, PD explode em k)
# O DC é O(2^n), n=20 já é 1 milhão, n=30 é 1 bilhão.
# Vamos limitar n=22.
N_MAX_GLOBAL = 22 
# ----------------------------------------------------

# --- 2. CRIAR A PASTA 'imagens' ---
IMG_DIR = "imagens"
if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)
    print(f"Pasta '{IMG_DIR}' criada.")
# -----------------------------------

print("--- INICIANDO BATERIA DE EXPERIMENTOS (SUBCONJUNTO SOMA) ---")

# Loop principal: 1 bateria de testes por "Par-Base"
for nome_run, (A_BASE, SOMA_ALVO_k) in PARES_DE_TESTE.items():
    
    n_max = min(len(A_BASE), N_MAX_GLOBAL)
    
    print(f"\n=================================================")
    print(f"  PROCESSANDO: {nome_run} (n_max={n_max}, k_alvo={SOMA_ALVO_k})")
    print(f"  Base A: {A_BASE[:n_max]}...")
    print(f"=================================================")

    tamanhos_n = [] # Eixo X (n)
    tempos_pd = []
    tempos_dc = []
    ops_pd = []
    ops_dc = []

    # Loop interno: testa os prefixos de n=1 até n=n_max
    for n in range(1, n_max + 1):
        
        A_atual = A_BASE[:n] # Pega o prefixo: A[0...n-1]
        
        print(f"\n  ... testando n = {n} (k={SOMA_ALVO_k})")
        print(f"    A: {A_atual}")

        # --- Roda PD ---
        pd_mod.cont_pd = 0
        start_time = time.time()
        res_pd = pd_mod.F_PD(A_atual, SOMA_ALVO_k)
        end_time = time.time()
        tempos_pd.append(end_time - start_time)
        ops_pd.append(pd_mod.cont_pd)
        print(f"    [PD] Ops: {pd_mod.cont_pd} | Tempo: {end_time - start_time:.4f}s | Res: {res_pd}")

        # --- Roda DC ---
        dc_mod.cont_dc = 0
        start_time = time.time()
        res_dc = dc_mod.F_DC(A_atual, n, SOMA_ALVO_k) # Passa 'n' (tamanho) e 'k'
        end_time = time.time()
        tempos_dc.append(end_time - start_time)
        ops_dc.append(dc_mod.cont_dc)
        print(f"    [DC] Ops: {dc_mod.cont_dc} | Tempo: {end_time - start_time:.4f}s | Res: {res_dc}")

        tamanhos_n.append(n)

    # --- Geração dos Gráficos ---
    print(f"Experimento com '{nome_run}' concluído. Gerando gráficos...")
    
    info_text = f"A_Base: {str(A_BASE[:n_max])}...\nSoma Alvo (k): {SOMA_ALVO_k}"
    path_tempo = os.path.join(IMG_DIR, f"grafico_tempo_{nome_run}.png")
    path_ops = os.path.join(IMG_DIR, f"grafico_operacoes_{nome_run}.png")

    # --- Gráfico de Tempo ---
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    ax.plot(tamanhos_n, tempos_pd, marker='o', label='PD (tempo)', color='red')
    ax.plot(tamanhos_n, tempos_dc, marker='o', label='DC (tempo)', color='blue')
    ax.set_title(f"Comparação de Tempo ({nome_run})")
    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Tempo (s)")
    ax.legend()
    ax.grid(True)
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(path_tempo)
    plt.close(fig)

    # --- Gráfico de Complexidade ---
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    ax.plot(tamanhos_n, ops_pd, marker='o', label='PD (operações)', color='red')
    ax.plot(tamanhos_n, ops_dc, marker='o', label='DC (chamadas)', color='blue')
    ax.set_title(f"Comparação de Complexidade ({nome_run})")
    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Número de operações/chamadas")
    ax.legend()
    ax.grid(True)
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(path_ops)
    plt.close(fig)

print("\n--- TODOS OS EXPERIMENTOS CONCLUÍDOS ---")

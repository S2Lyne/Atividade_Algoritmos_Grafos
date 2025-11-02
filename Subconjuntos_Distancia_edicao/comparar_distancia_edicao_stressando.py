import time
import matplotlib.pyplot as plt
import os
import distancia_edicao_PD as pd_mod
import distancia_edicao_DC as dc_mod

# --- 1. DEFINA AQUI OS PARES PARA OS EXPERIMENTOS ---
PARES_DE_TESTE = {
    # Run 1: O que já testamos
    "run_1_algoritmo": ("ALGORITMOS", "LOGARITMOS"),
    # Run 2: O exemplo dos slides (note como n=7, m=6)
    "run_2_slide": ("ABBBAAB", "BBAABB"),
    # Run 3: Palavras totalmente diferentes
    "run_3_diferente": ("BAHIA", "VITORIA"),
    # Run 4: Palavras quase iguais
    "run_4_similar": ("COMPUTACAO", "COMPUTADOR")
}

# Limite de sanidade: O DC(n=10) já deu 12 Milhões de chamadas.
# Não vamos passar disso para não travar.
N_MAX_GLOBAL = 10 
# ----------------------------------------------------

# --- 2. Salvar gráficos na pasta 'imagens' ---
IMG_DIR = "imagens"
# -----------------------------------

print("--- INICIANDO BATERIA DE EXPERIMENTOS (DISTÂNCIA DE EDIÇÃO) ---")

# Loop principal: 1 bateria de testes por "Par-Base"
for nome_run, (X_BASE, Y_BASE) in PARES_DE_TESTE.items():
    
    # Pega o menor tamanho entre as duas strings e limita ao N_MAX_GLOBAL
    n_max = min(len(X_BASE), len(Y_BASE), N_MAX_GLOBAL)
    
    print(f"\n=================================================")
    print(f"  PROCESSANDO: {nome_run} (n_max={n_max})")
    print(f"  Base X: {X_BASE}")
    print(f"  Base Y: {Y_BASE}")
    print(f"=================================================")

    tamanhos_n_total = [] # Eixo X (m+n)
    tempos_pd = []
    tempos_dc = []
    ops_pd = []
    ops_dc = []

    # Loop interno: testa os prefixos de n=1 até n=n_max
    for n in range(1, n_max + 1):
        
        # Pega o prefixo de CADA string
        # (O "m" do slide será igual ao "n" aqui)
        X_atual = X_BASE[:n] 
        Y_atual = Y_BASE[:n]
        m = n # m == n
        
        tamanho_entrada = n + m # m+n
        tamanhos_n_total.append(tamanho_entrada)
        
        print(f"\n  ... testando n={n}, m={m} (m+n = {tamanho_entrada})")
        print(f"    X: {X_atual}")
        print(f"    Y: {Y_atual}")

        # --- Roda PD ---
        pd_mod.cont_pd = 0
        start_time = time.time()
        dist_pd = pd_mod.C_ij_PD(X_atual, Y_atual)
        end_time = time.time()
        tempos_pd.append(end_time - start_time)
        ops_pd.append(pd_mod.cont_pd)
        print(f"    [PD] Ops: {pd_mod.cont_pd} | Tempo: {end_time - start_time:.4f}s | Dist: {dist_pd}")

        # --- Roda DC ---
        # Sim, o código manda a mesma entrada para os dois.
        dc_mod.cont_dc = 0
        start_time = time.time()
        dist_dc = dc_mod.C_ij_DC(X_atual, n, Y_atual, m) # Passa n e m
        end_time = time.time()
        tempos_dc.append(end_time - start_time)
        ops_dc.append(dc_mod.cont_dc)
        print(f"    [DC] Ops: {dc_mod.cont_dc} | Tempo: {end_time - start_time:.4f}s | Dist: {dist_dc}")

    # --- Geração dos Gráficos ---
    print(f"Experimento com '{nome_run}' concluído. Gerando gráficos...")
    
    # --- 3. TEXTO E NOME DO ARQUIVO ATUALIZADOS ---
    info_text = f"X_Base: {X_BASE} | Y_Base: {Y_BASE}"
    path_tempo = os.path.join(IMG_DIR, f"grafico_tempo_{nome_run}.png")
    path_ops = os.path.join(IMG_DIR, f"grafico_operacoes_{nome_run}.png")

    # --- Gráfico de Tempo ---
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    ax.plot(tamanhos_n_total, tempos_pd, marker='o', label='PD (tempo)', color='red')
    ax.plot(tamanhos_n_total, tempos_dc, marker='o', label='DC (tempo)', color='blue')
    ax.set_title(f"Comparação de Tempo ({nome_run})")
    ax.set_xlabel("Tamanho da entrada (m+n)")
    ax.set_ylabel("Tempo (s)")
    ax.legend()
    ax.grid(True)
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(path_tempo) # Salva na pasta 'imagens/'
    plt.close(fig)

    # --- Gráfico de Complexidade ---
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    ax.plot(tamanhos_n_total, ops_pd, marker='o', label='PD (operações)', color='red')
    ax.plot(tamanhos_n_total, ops_dc, marker='o', label='DC (chamadas)', color='blue')
    ax.set_title(f"Comparação de Complexidade ({nome_run})")
    ax.set_xlabel("Tamanho da entrada (m+n)")
    ax.set_ylabel("Número de operações/chamadas")
    ax.legend()
    ax.grid(True)
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(path_ops) # Salva na pasta 'imagens/'
    plt.close(fig)

print("\n--- TODOS OS EXPERIMENTOS CONCLUÍDOS ---")
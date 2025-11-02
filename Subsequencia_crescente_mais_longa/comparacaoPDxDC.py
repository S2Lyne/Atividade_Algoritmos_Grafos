import time
import matplotlib.pyplot as plt
import random
import subsequenciaMaisLongaPD as pd_mod
import subsequenciaMaisLongaDC as dc_mod

# --- CONFIGURAÇÃO ---
# Quantas vezes queremos rodar o experimento COMPLETO?
NUM_RUNS = 3
N_MAXIMO = 14 # Vá até 14 (depois disso o DC demora demais)
# --------------------

# Envolvemos tudo num loop FOR principal
for run_num in range(1, NUM_RUNS + 1):
    print(f"\n=================================================")
    print(f"  INICIANDO BATERIA DE TESTES (RUN {run_num} / {NUM_RUNS}) ")
    print(f"=================================================")
    
    entradas = []
    tamanhos_n = list(range(1, N_MAXIMO + 1)) 

    for n in tamanhos_n:
        X = [random.randint(1, 100) for _ in range(n)]
        entradas.append(X)

    tempos_pd = []
    tempos_dc = []
    ops_pd = []
    ops_dc = []

    print("Iniciando experimentos...")

    for X in entradas:
        n = len(X)
        print(f"====== Testando n = {n} ======")

        # --- Programação Dinâmica ---
        pd_mod.cont_pd = 0 
        start_time = time.time()
        pd_mod.subsequencia_mais_longa(X, 0, n-1) 
        end_time = time.time()
        tempos_pd.append(end_time - start_time)
        ops_pd.append(pd_mod.cont_pd) 

        # --- Divisão e Conquista ---
        dc_mod.cont_dc = 0 
        start_time = time.time()
        dc_mod.Cresc_long(X, 0, n-1) 
        end_time = time.time()
        tempos_dc.append(end_time - start_time)
        ops_dc.append(dc_mod.cont_dc) 

    print("Experimentos concluídos. Gerando gráficos...")

    # --- Gráfico de tempo de execução ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({'font.size': 12})
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos_n, tempos_pd, marker='o', label='PD (tempo)', color='red')
    plt.plot(tamanhos_n, tempos_dc, marker='o', label='DC (tempo)', color='blue')
    plt.title(f"Comparação de Tempo de Execução (Run {run_num})") # Título atualizado
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo (s)")
    plt.legend()
    plt.grid(True)
    # Nome do arquivo atualizado
    plt.savefig(f"comparacao_tempo_run_{run_num}.png") 
    plt.close() 

    # --- Gráfico de complexidade experimental ---
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos_n, ops_pd, marker='o', label='PD (operações)', color='red')
    plt.plot(tamanhos_n, ops_dc, marker='o', label='DC (chamadas)', color='blue')
    plt.title(f"Comparação de Complexidade (Run {run_num})") # Título atualizado
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Número de operações/chamadas")
    plt.legend()
    plt.grid(True)
    # Nome do arquivo atualizado
    plt.savefig(f"comparacao_operacoes_run_{run_num}.png") 
    plt.close() 

    print(f"Gráficos da Run {run_num} salvos.")

print("\nTODAS AS BATERIAS DE TESTE CONCLUÍDAS.")
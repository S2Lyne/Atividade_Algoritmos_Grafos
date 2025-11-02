# comparar_distancia_edicao.py
import time
import os
import matplotlib.pyplot as plt
import distancia_edicao_PD as pd_mod
import distancia_edicao_DC as dc_mod

# --- CONFIGURAÇÃO ---
# Define as strings-base para o experimento
# (O DC explode MUITO rápido, N=8 (m+n=16) já pode demorar minutos)
X_BASE = "ALGORITMOS"
Y_BASE = "LOGARITMOS"
N_MAXIMO = min(len(X_BASE), len(Y_BASE)) # Vamos testar até o prefixo máximo
# --------------------

# --- 2. Salvar gráficos na pasta 'imagens' ---
IMG_DIR = "imagens"
# -----------------------------------

print("--- INICIANDO EXPERIMENTO (DISTÂNCIA DE EDIÇÃO) ---")
print(f"Base X: {X_BASE}")
print(f"Base Y: {Y_BASE}")
print("=================================================")

tamanhos_n_total = [] # Eixo X (vai ser m+n)
tempos_pd = []
tempos_dc = []
ops_pd = []
ops_dc = []

# Loop interno: testa os prefixos de n=1 até n=N_MAXIMO
for n in range(1, N_MAXIMO + 1):
    
    # Pega o prefixo: X[0...n-1] e Y[0...n-1]
    X_atual = X_BASE[:n] 
    Y_atual = Y_BASE[:n]
    
    # O tamanho da entrada é m+n 
    tamanho_entrada = len(X_atual) + len(Y_atual)
    tamanhos_n_total.append(tamanho_entrada)
    
    print(f"\n... testando n={n} (m+n = {tamanho_entrada})")
    print(f"  X: {X_atual}")
    print(f"  Y: {Y_atual}")

    # --- Roda PD ---
    pd_mod.cont_pd = 0
    start_time = time.time()
    # Chama a função PD (que recebe as strings inteiras)
    dist_pd = pd_mod.C_ij_PD(X_atual, Y_atual)
    end_time = time.time()
    tempos_pd.append(end_time - start_time)
    ops_pd.append(pd_mod.cont_pd)
    print(f"  [PD] Ops: {pd_mod.cont_pd} | Tempo: {end_time - start_time:.4f}s | Dist: {dist_pd}")

    # --- Roda DC ---
    dc_mod.cont_dc = 0
    start_time = time.time()
    # Chama a função DC (que recebe os tamanhos n e m)
    dist_dc = dc_mod.C_ij_DC(X_atual, n, Y_atual, n)
    end_time = time.time()
    tempos_dc.append(end_time - start_time)
    ops_dc.append(dc_mod.cont_dc)
    print(f"  [DC] Ops: {dc_mod.cont_dc} | Tempo: {end_time - start_time:.4f}s | Dist: {dist_dc}")

# --- Geração dos Gráficos ---
print("\nExperimento concluído. Gerando gráficos...")
info_text = f"X_Base: {X_BASE} | Y_Base: {Y_BASE}"

# --- Gráfico de Tempo ---
fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.2) 
ax.plot(tamanhos_n_total, tempos_pd, marker='o', label='PD (tempo)', color='red')
ax.plot(tamanhos_n_total, tempos_dc, marker='o', label='DC (tempo)', color='blue')
ax.set_title("Comparação de Tempo (Distância de Edição)")
ax.set_xlabel("Tamanho da entrada (m+n)")
ax.set_ylabel("Tempo (s)")
ax.legend()
ax.grid(True)
plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
plt.savefig("grafico_tempo_distancia_edicao.png")
plt.close(fig)

# --- Gráfico de Complexidade ---
fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.2) 
ax.plot(tamanhos_n_total, ops_pd, marker='o', label='PD (operações)', color='red')
ax.plot(tamanhos_n_total, ops_dc, marker='o', label='DC (chamadas)', color='blue')
ax.set_title("Comparação de Complexidade (Distância de Edição)")
ax.set_xlabel("Tamanho da entrada (m+n)")
ax.set_ylabel("Número de operações/chamadas")
ax.legend()
ax.grid(True)
plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
plt.savefig("grafico_operacoes_distancia_edicao.png")
plt.close(fig)

print("--- GRÁFICOS SALVOS ---")
print("grafico_tempo_distancia_edicao.png")
print("grafico_operacoes_distancia_edicao.png")
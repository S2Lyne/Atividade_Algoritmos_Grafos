import time
import matplotlib.pyplot as plt
import subsequenciaMaisLongaPD as pd_mod
import subsequenciaMaisLongaDC as dc_mod

# --- DEFINA AQUI AS "LISTAS-BASE" PARA OS EXPERIMENTOS ---
# Vamos rodar o experimento completo para cada uma destas listas
LISTAS_DE_TESTE = {
    # Lista 1: A sua original
    "lista_1": [1, 3, 2, 7, 10, 14, 8, 31, 5, 4, 12, 11, 15],
    # Lista 2: A sua segunda sugestão (com 15 itens)
    "lista_2": [9, 2, 3, 7, 10, 14, 20, 8, 31, 44, 50, 77, 13, 22, 35],
    # Lista 3: Um "pior caso" para o DC (crescente)
    "lista_3": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    # Lista 4: Um "melhor caso" para o DC (decrescente)
    "lista_4": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}
# ---------------------------------------------------------

print("--- INICIANDO EXPERIMENTO POR PREFIXO ---")

# Loop principal: 1 bateria de testes por "Lista-Base"
for nome_lista, lista_base in LISTAS_DE_TESTE.items():
    
    n_max = len(lista_base)
    print(f"\n=================================================")
    print(f"  PROCESSANDO: {nome_lista} (tamanho total {n_max}) ")
    print(f"  Base: {lista_base}")
    print(f"=================================================")

    tamanhos_n = []
    tempos_pd = []
    tempos_dc = []
    ops_pd = []
    ops_dc = []

    # Loop interno: testa os prefixos de n=1 até n=n_max
    for n in range(1, n_max + 1):
        
        # É ASSIM que se "varia o tamanho da entrada"
        X_atual = lista_base[:n] # Pega o prefixo: X[0...n-1]
        print(f"  ... testando n = {n} (Entrada: {X_atual})")

        # --- Roda PD ---
        pd_mod.cont_pd = 0
        start_time = time.time()
        pd_mod.subsequencia_mais_longa(X_atual, 0, n - 1)
        end_time = time.time()
        tempos_pd.append(end_time - start_time)
        ops_pd.append(pd_mod.cont_pd)

        # --- Roda DC ---
        dc_mod.cont_dc = 0
        start_time = time.time()
        dc_mod.Cresc_long(X_atual, 0, n - 1)
        end_time = time.time()
        tempos_dc.append(end_time - start_time)
        ops_dc.append(dc_mod.cont_dc)

        tamanhos_n.append(n)

    # --- Geração dos Gráficos para esta Lista-Base ---
    print(f"Experimento com '{nome_lista}' concluído. Gerando gráficos...")
    
    # Esta é a informação que você pediu para adicionar na imagem
    info_text = f"Lista-Base: {str(lista_base):.150s}" # Corta se for muito longa

    # --- Gráfico de Tempo ---
    # (Ajusta o espaço 'bottom' para caber o texto)
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    
    ax.plot(tamanhos_n, tempos_pd, marker='o', label='PD (tempo)', color='red')
    ax.plot(tamanhos_n, tempos_dc, marker='o', label='DC (tempo)', color='blue')
    ax.set_title(f"Comparação de Tempo (Base: {nome_lista})")
    ax.set_xlabel("Tamanho do prefixo (n)")
    ax.set_ylabel("Tempo (s)")
    ax.legend()
    ax.grid(True)
    
    # ONDE A MÁGICA ACONTECE: Adiciona o texto no rodapé
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(f"grafico_tempo_{nome_lista}.png")
    plt.close(fig)

    # --- Gráfico de Complexidade ---
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.2) 
    
    ax.plot(tamanhos_n, ops_pd, marker='o', label='PD (operações)', color='red')
    ax.plot(tamanhos_n, ops_dc, marker='o', label='DC (chamadas)', color='blue')
    ax.set_title(f"Comparação de Complexidade (Base: {nome_lista})")
    ax.set_xlabel("Tamanho do prefixo (n)")
    ax.set_ylabel("Número de operações/chamadas")
    ax.legend()
    ax.grid(True)
    
    # Adiciona o texto no rodapé
    plt.figtext(0.5, 0.01, info_text, wrap=True, ha='center', fontsize=9)
    plt.savefig(f"grafico_operacoes_{nome_lista}.png")
    plt.close(fig)

print("\n--- TODOS OS EXPERIMENTOS CONCLUÍDOS ---")
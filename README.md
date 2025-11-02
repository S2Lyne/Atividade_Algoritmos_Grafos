# Atividade: Análise Experimental de Divisão e Conquista vs. Programação Dinâmica

Este repositório contém as implementações e a análise experimental para a atividade da disciplina **IC0004 - Algoritmos e Grafos**, ministrada pelo Prof. George Lima.

O objetivo deste projeto é comparar experimentalmente o desempenho de algoritmos de Divisão e Conquista (DC) puros (recursivos, *top-down*) contra suas implementações equivalentes usando Programação Dinâmica (PD) (*bottom-up*).

A análise foca em como a abordagem de PD resolve eficientemente o problema de **subproblemas sobrepostos** (overlapping subproblems), evitando o recálculo que leva as implementações de DC a uma complexidade exponencial.

## 🎯 Problemas Implementados

Os experimentos foram realizados para os três problemas propostos, e os gráficos de complexidade (número de operações vs. tamanho da entrada) foram gerados para cada um:

1.  **Subsequência Crescente Mais Longa** (LIS)
    * PD: Implementação $\Theta(n^2)$
    * DC: Implementação $\Theta(2^n)$

2.  **Distância de Edição** (Edit Distance)
    * PD: Implementação $\Theta(nm)$
    * DC: Implementação $\Theta(3^{n+m})$

3.  **Subconjunto Soma** (Subset Sum)
    * PD: Implementação pseudo-polinomial $\Theta(nk)$
    * DC: Implementação $\Theta(2^n)$

## 📂 Estrutura do Repositório

* `/Subsequencia_crescente_mais_longa`: Contém os scripts `...PD.py`, `...DC.py` e o comparador do Problema 1.
* `/Distancia_edicao`: Contém os scripts `...PD.py`, `...DC.py` e os comparadores do Problema 2.
* `/Subconjunto_soma`: Contém os scripts `...PD.py`, `...DC.py` e o comparador do Problema 3.
* `/imagens`: Contém todos os gráficos `.png` gerados pelos experimentos, separados por problema.
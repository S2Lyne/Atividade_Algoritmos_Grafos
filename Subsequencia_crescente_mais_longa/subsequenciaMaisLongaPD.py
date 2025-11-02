# subsequencia-mais-longa-PD.py
import time

cont_pd = 0


def subsequencia_mais_longa(X, a, b):
    """
    Implementação PD (bottom-up) da formulação do slide.
    Mantém a assinatura (X, a, b) e trabalha no intervalo [a..b].
    Retorna a subsequência crescente mais longa (lista).
    """

    if X == [] or a > b:
        return []

    
    global cont_pd
    
    # Trabalhar apenas no segmento X[a..b]
    n = b - a + 1
    # T[i] corresponde ao tamanho da LIS que termina em X[a + i]
    T = [0] * n
    # S[i] guarda a subsequência (lista) que termina em X[a+i]
    S = [[] for _ in range(n)]

    # S0: versão com -inf no início, como no slide, para comparações fáceis (opcional)
    # mas aqui vamos comparar usando X[a+i] diretamente.
    for i in range(n):
        # i corresponde a índice relativo; índice absoluto = a + i
        maxt = 0
        maxi = -1
        j = 0
        # percorre j < i
        while j < i:
            cont_pd += 1
            # índice absoluto
            if X[a + i] > X[a + j] and T[j] > maxt:
                maxt = T[j]
                maxi = j
            j += 1

        T[i] = maxt + 1
        if maxi != -1:
            S[i] = S[maxi] + [X[a + i]]
        else:
            S[i] = [X[a + i]]

        # impressão opcional passo-a-passo (remove se quiser saída mais limpa)
        # print(f"PD: i_abs={a+i}, X[i]={X[a+i]}, T[{i}]={T[i]}, S[{i}]={S[i]}")

    # escolhe a subsequência máxima
    idx = max(range(n), key=lambda k: T[k])
    #print("PD: T final =", T)
    return S[idx]

if __name__ == "__main__":
    X = [1,3,2,7,10,14,8,31]
    
    print(X)
    
    start_time = time.time()
    
    kl = subsequencia_mais_longa(X, 0, len(X)-1)
    end_time = time.time()
    print("PD -> subsequência mais longa:", kl)
    print("Tempo de execução:", end_time - start_time)
    print("Operações PD:", cont_pd)

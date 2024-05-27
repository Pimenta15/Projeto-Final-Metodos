import time
import numpy as np

class ResolverDD:
    def __init__(self, pontos_conhecidos):
        self.x = [p[0] for p in pontos_conhecidos]
        self.y = [p[1] for p in pontos_conhecidos]

    def interpolar(self, xdafuncao):
        start_time = time.time()  # Início da medição do tempo
        n = len(self.x)
        fdd = np.zeros((n, n))  # Cria a matriz de diferenças divididas
        for i in range(n):
            fdd[i][0] = self.y[i]

        for j in range(1, n):
            for i in range(n - j):
                fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (self.x[i + j] - self.x[i])

        xterm = 1
        y0 = fdd[0][0]  # y0
        for i in range(1, n):
            xterm = xterm * (xdafuncao - self.x[i - 1])
            y0 = y0 + fdd[0][i] * xterm

        time.sleep(1)
        end_time = time.time()  # Fim da medição do tempo
        tempo_execucao = end_time - start_time

        return y0, tempo_execucao  # Retorna p(x) e o tempo de execução

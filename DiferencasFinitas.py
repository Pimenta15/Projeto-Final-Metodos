import numpy as np
import time

class ResolverDF:
    def __init__(self, pontos_conhecidos):
        self.x = [p[0] for p in pontos_conhecidos]
        self.y = [p[1] for p in pontos_conhecidos]

    def fatorial_iterativo(self, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i  # Corrigido para multiplicar
        return resultado

    def calcular_diferencas_finitas(self):
        n = len(self.x)
        diferencas = np.zeros((n, n))
        diferencas[:, 0] = self.y

        for j in range(1, n):
            for i in range(n - j):
                diferencas[i, j] = diferencas[i + 1, j - 1] - diferencas[i, j - 1]

        self.diferencas = diferencas
        return diferencas

    def interpolar(self, xdafuncao):
        start_time = time.time()
        self.calcular_diferencas_finitas()
        n = len(self.x)
        h = self.x[1] - self.x[0]  # assumindo que x está igualmente espaçado
        s = (xdafuncao - self.x[0]) / h

        resultado = self.diferencas[0, 0]
        termo = 1  # Inicializando como 1 para o produto

        for i in range(1, n):
            termo *= (s - (i - 1))
            resultado += (termo / self.fatorial_iterativo(i)) * self.diferencas[0, i]

        time.sleep(1)
        end_time = time.time() - start_time 
        return resultado, end_time

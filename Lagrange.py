import numpy as np
import time

class resolver:
    def __init__(self, pontos_conhecidos):
        self.pontos_conhecidos = pontos_conhecidos

    def interpolar(self, x):
        start_time = time.time() 
        n_medidas = len(self.pontos_conhecidos)
        for _ in range(n_medidas):
            

            n = len(self.pontos_conhecidos)
            resultado = 0

            for i in range(n):
                xi, yi = self.pontos_conhecidos[i]
                termo = yi

                for j in range(n):
                    if i != j:
                        xj, _ = self.pontos_conhecidos[j]
                        termo *= (x - xj) / (xi - xj)

                resultado += termo
        time.sleep(1)
        end_time = time.time()  # Fim da medição do tempo
        tempo_execucao = end_time - start_time
        return resultado, tempo_execucao


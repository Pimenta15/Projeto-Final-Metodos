import numpy as np
import time

class Interpolacao:
    def __init__(self, pontos_conhecidos):
        self.pontos_conhecidos = pontos_conhecidos

    def interpolar(self, x):
        pass

class InterpolacaoLagrange(Interpolacao):
    def interpolar(self, x):
        start_time = time.time()  # Início da medição do tempo
        n = len(self.pontos_conhecidos)
        resultado = 0
        for i in range(n):
            xi, yi = self.pontos_conhecidos[i]
            li = 1
            for j in range(n):
                if i != j:
                    xj, _ = self.pontos_conhecidos[j]
                    li *= (x - xj) / (xi - xj)
            resultado += yi * li
        end_time = time.time()  # Fim da medição do tempo
        tempo_execucao = end_time - start_time
        return resultado, tempo_execucao

# Adicione as outras classes de interpolação aqui (ex: InterpolacaoQuadratica, InterpolacaoDiferencasDivididas, InterpolacaoDiferencasFinitas)

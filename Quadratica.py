import numpy as np
import time
from Metodos import MetodoDireto, MetodoIterativo

class InterpolacaoQuadratica:
    def __init__(self, pontos_conhecidos):
        self.pontos_conhecidos = pontos_conhecidos

    def interpolar(self, x, metodo='direto'):
        start_time = time.time()  # Início da medição do tempo

        # Construir o sistema linear Ax = b para a interpolação quadrática
        A = []
        b = []

        for xi, yi in self.pontos_conhecidos:
            A.append([xi**2, xi, 1])
            b.append(yi)

        A = np.array(A)
        b = np.array(b)

        # Resolver o sistema linear
        if metodo == 'direto':
            solver = MetodoDireto(A, b)
        elif metodo == 'iterativo':
            solver = MetodoIterativo(A, b)
        else:
            raise ValueError("Método desconhecido. Use 'direto' ou 'iterativo'.")

        coeficientes = solver.resolver()

        a, b, c = coeficientes
        resultado = a * x**2 + b * x + c

        end_time = time.time()  # Fim da medição do tempo
        tempo_execucao = end_time - start_time

        return resultado, tempo_execucao

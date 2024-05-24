# arquivo: sistema_linear.py

class SistemaLinear:
    def __init__(self, matriz_coeficientes, vetor_independente):
        self.matriz_coeficientes = matriz_coeficientes
        self.vetor_independente = vetor_independente

    def resolver(self):
        pass

class MetodoDireto(SistemaLinear):
    def resolver(self):
        # Implementar método direto (por exemplo, Gauss-Jordan)
        pass

class MetodoIterativo(SistemaLinear):
    def resolver(self):
        # Implementar método iterativo (por exemplo, Jacobi ou Seidel)
        pass

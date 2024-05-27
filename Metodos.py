import numpy as np

class MetodoDireto:
    def __init__(self, A, b):
        self.A = A.astype(np.float64)  # Garantir que A seja float64
        self.b = b.astype(np.float64)  # Garantir que b seja float64

    def resolver(self):
        A = self.A.copy()
        b = self.b.copy()
        n = len(b)

        for i in range(n):
            # Pivot
            max_row = np.argmax(np.abs(A[i:, i])) + i
            if A[max_row, i] == 0:
                raise ValueError("Matriz é singular e não pode ser resolvida.")
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

            # Eliminação
            for j in range(i + 1, n):
                ratio = A[j, i] / A[i, i]
                A[j, i:] -= ratio * A[i, i:]
                b[j] -= ratio * b[i]

        # Resolução do sistema triangular superior
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        return x



class MetodoIterativo:
    def __init__(self, A, b, max_iter=50, tol=1e-2):
        self.A = A.astype(np.float64)  # Garantir que A seja float64
        self.b = b.astype(np.float64)  # Garantir que b seja float64
        self.max_iter = max_iter
        self.tol = tol

    def resolver(self):
        A = self.A
        b = self.b
        n = len(b)
        x = np.zeros(n)
        
        for iteration in range(self.max_iter):
            x_old = x.copy()
            for i in range(n):
                if A[i, i] == 0:
                    raise ValueError(f"Elemento diagonal zero encontrado em A[{i},{i}], método não pode proceder.")
                s1 = np.dot(A[i, :i], x_old[:i])  # Utiliza a estimativa anterior de x
                s2 = np.dot(A[i, i+1:], x_old[i+1:])  # Utiliza a estimativa anterior de x
                x[i] = (b[i] - s1 - s2) / A[i, i]
            # Verificação de convergência
            if np.linalg.norm(x - x_old, ord=np.inf) < self.tol:
                print(f"Convergência alcançada após {iteration + 1} iterações.")
                return x

        print(f"Número máximo de iterações atingido ({self.max_iter}).")
        return x  # Retorna a última iteração se não convergir

# Exemplo de uso
A = np.array([[3, 1, -1],
              [1, 4, -2],
              [-1, 1, 5]], dtype=np.float64)
b = np.array([1, -5, 3], dtype=np.float64)

metodo = MetodoJacobi(A, b)
solucao = metodo.resolver()
print("Solução:", solucao)

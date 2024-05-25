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

import numpy as np

class MetodoIterativo:
    def __init__(self, A, b, max_iter=10000, tol=1e-10):
        self.A = A.astype(np.float64)  # Garantir que A seja float64
        self.b = b.astype(np.float64)  # Garantir que b seja float64
        self.max_iter = max_iter
        self.tol = tol

    def resolver(self):
        A = self.A
        b = self.b
        n = len(b)
        x = np.zeros(n)
        x_new = np.zeros(n)

        for _ in range(self.max_iter):
            for i in range(n):
                s1 = np.dot(A[i, :i], x[:i])
                s2 = np.dot(A[i, i+1:], x[i+1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]

            if np.linalg.norm(x_new - x, ord=np.inf) < self.tol:
                return x_new

            x = x_new.copy()

        raise ValueError("O método de Jacobi não convergiu")


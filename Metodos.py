import numpy as np

class MetodoDireto:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def resolver(self):
        A = self.A.copy()
        b = self.b.copy()
        n = len(b)

        # Eliminação de Gauss
        for i in range(n):
            # Pivotamento parcial
            max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
            if i != max_row:
                A[[i, max_row]] = A[[max_row, i]]
                b[i], b[max_row] = b[max_row], b[i]

            # Eliminar subdiagonal
            for j in range(i+1, n):
                ratio = A[j][i] / A[i][i]
                A[j][i:] -= ratio * A[i][i:]
                b[j] -= ratio * b[i]

        # Substituição regressiva
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]

        return x

class MetodoIterativo:
    def __init__(self, A, b, max_iter=1000, tol=1e-10):
        self.A = A
        self.b = b
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

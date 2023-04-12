class NewtonMethod:
    def __init__(self, equations, jacobian, x0, eps=0.01, max_iter=100):
        self.equations = equations
        self.jacobian = jacobian
        self.x = x0
        self.eps = eps
        self.max_iter = max_iter

    def solve(self):
        for i in range(self.max_iter):
            fx = self.equations(self.x)
            if all(abs(fi) < self.eps for fi in fx):
                return tuple(self.x)
            Jx = self.jacobian(self.x)
            try:
                dx = self.solve_system(Jx, fx)
            except ValueError:
                raise Exception("Linear system is singular")
            self.x = [x - d for x, d in zip(self.x, dx)]
        raise Exception("Maximum number of iterations exceeded")

    @staticmethod
    def solve_system(A, b):
        n = len(b)
        for i in range(n):
            max_el = abs(A[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > max_el:
                    max_el = abs(A[k][i])
                    max_row = k
            if max_el == 0:
                raise ValueError("Matrix is singular")
            for k in range(i, n):
                tmp = A[max_row][k]
                A[max_row][k] = A[i][k]
                A[i][k] = tmp
            tmp = b[max_row]
            b[max_row] = b[i]
            b[i] = tmp
            for k in range(i + 1, n):
                c = -A[k][i] / A[i][i]
                for j in range(i, n):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]
                b[k] += c * b[i]
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = b[i] / A[i][i]
            for k in range(i - 1, -1, -1):
                b[k] -= A[k][i] * x[i]
        return x


def equations(x):
    return [x[0] ** 2 + x[1] ** 2 - 1, x[0] ** 2 - x[1] ** 2]


def jacobian(x):
    return [[2 * x[0], 2 * x[1]], [2 * x[0], -2 * x[1]]]


if __name__ == '__main__':
    solver = NewtonMethod(equations=equations, jacobian=jacobian, x0=[-10, -1])
    x = solver.solve()
    print(x)

